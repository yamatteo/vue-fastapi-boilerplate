from typing import Optional

from fastapi import APIRouter, Depends, Body

from models import User, Content, Node, Group
from routers import get_current_user, admin_only

#
router = APIRouter()


@router.post("/push_content")
async def push_content(node_id: str = Body(..., embed=True), content_id: str = Body(..., embed=True),
                       admin: User = Depends(admin_only)):
    assert admin is not None
    node = await Node.find_one_and_add_to_set(
        find={"id": node_id},
        data={"contents": Content.ref(content_id)}
    )
    return node.export()


@router.post("/pull_content")
async def pull_content(node_id: str = Body(..., embed=True), content_id: str = Body(..., embed=True),
                    admin: User = Depends(admin_only)):
    assert admin is not None
    node = await Node.find_one_and_pull(
        find={"id": node_id},
        data={"contents": Node.ref(content_id)}
    )
    return node.export()


@router.get("/current")
async def current_nodes(current_user: User = Depends(get_current_user)):
    groups = await Group.find({"members": current_user})
    nodes_ids = [node.id for group in groups for node in group.nodes]
    return [node.export() for node in await Node.find({"id": {"$in": nodes_ids}})]


@router.get("/browse")
async def browse_nodes():
    return [node.export() for node in await Node.find({})]


@router.get("/read")
async def read_node(node_id: str):
    return await Node.find_one({"id": node_id})


@router.post("/add")
async def add_node(short: str, long: Optional[str] = "", admin: User = Depends(admin_only)):
    assert admin is not None
    return await Node.insert_one({"short": short, "long": long})


@router.post("/edit")
async def edit_node(node_id: str, short: Optional[str] = None, long: Optional[str] = None,
                    admin: User = Depends(admin_only)):
    assert admin is not None
    data = {}
    if short is not None:
        data["short"] = short
    if long is not None:
        data["long"] = long
    return await Node.find_one_and_set(find={"id": node_id}, data=data)


@router.post("/delete")
async def delete_node(node_id: str, admin: User = Depends(admin_only)):
    assert admin is not None
    return await Node.delete_one({"id": node_id})
