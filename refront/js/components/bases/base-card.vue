<template>
  <b-card
    header-tag="header"
    class="mb-2"
    :style="scroll ? `max-height: ${max_height}; overflow-y: auto;` : ``"
    no-body
  >
    <template v-slot:header>
      <slot name="header">
        <div class="d-flex align-items-center">
          <span
            class="h5 m-0 flex-grow-1"
            :style="forced ? '' : 'cursor: pointer;'"
            @click="header_click"
          >{{ title }}</span>
          <slot name="pills"></slot>
        </div>
      </slot>
    </template>
    <b-card-body v-if="show_body">
      <b-overlay :show="over_body">
      <slot>
        <slot name="empty">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel elementum turpis. Maecenas porttitor leo leo, sit amet dictum massa interdum in. Etiam efficitur pellentesque mi ac lacinia. Nam aliquam auctor massa ut vestibulum. Integer efficitur quis magna id blandit. Cras sed leo non massa ultricies venenatis sit amet eget turpis. Mauris sit amet sem vitae purus sagittis rutrum. Ut scelerisque lobortis massa, nec aliquet arcu facilisis nec. Nam ut sapien rhoncus, maximus eros non, volutpat turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam finibus lacus tincidunt tortor porta finibus. In eget magna eleifend, convallis magna sed, venenatis libero. Etiam lobortis nulla lorem, non laoreet nunc dapibus nec.</p>
          <p>Nunc egestas vestibulum efficitur. Donec nec odio aliquam, aliquam tellus at, fringilla arcu. Pellentesque luctus mattis posuere. Duis dapibus vitae felis in facilisis. Vestibulum semper lorem non bibendum maximus. Fusce dapibus, risus sit amet laoreet posuere, enim turpis ultricies neque, non convallis quam enim in leo. Morbi sodales justo et tempus bibendum. Aliquam vulputate sem eget erat porta lobortis. Aenean euismod tortor vitae vestibulum condimentum. Maecenas ut est lacus. Fusce fringilla lobortis sapien, eu pretium mi fermentum sit amet. Duis vestibulum magna turpis, quis varius eros malesuada vitae. Vestibulum tristique, dui eget convallis euismod, dui sapien volutpat nisi, non dictum nibh elit vel tortor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Integer pretium urna sed tellus laoreet sollicitudin. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
          <p>Donec rutrum quis dolor a fringilla. Curabitur tincidunt sagittis nisi, quis placerat nibh rhoncus et. Mauris lacinia est ac dictum scelerisque. Praesent scelerisque enim ac facilisis lobortis. Maecenas ligula neque, feugiat et lectus vel, tempor molestie erat. Duis a nisi leo. Phasellus fringilla tortor vel nisl condimentum semper nec et odio. Nulla pellentesque sem facilisis metus laoreet rutrum.</p>
          <p>Etiam enim lacus, feugiat at magna vel, faucibus ultricies elit. Nullam luctus elit a arcu rutrum tristique. Maecenas blandit venenatis lectus, volutpat eleifend lacus consequat non. Maecenas sit amet elementum nulla. Proin et felis quis mauris ornare porta. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec non lectus metus. Sed ex est, congue sed consectetur et, luctus nec ipsum. Etiam dui est, commodo sit amet massa id, rutrum cursus ligula. In hac habitasse platea dictumst. Pellentesque pretium iaculis purus, quis finibus lorem finibus vitae. Aenean vulputate varius tortor non sodales. Integer viverra est at massa gravida sollicitudin. Etiam id odio in ipsum hendrerit imperdiet sit amet eget ligula. Fusce interdum massa arcu, in euismod nunc auctor gravida. Morbi sit amet lacinia velit.</p>
          <p>Nulla facilisi. Donec cursus sapien velit, at varius augue venenatis vitae. Nunc luctus nulla urna, sed dapibus sem accumsan quis. In ut dapibus urna. Curabitur quis tincidunt justo, tempus eleifend ante. Aenean fringilla volutpat mauris eget tristique. Fusce eu vehicula ante. Nunc pretium est id quam pulvinar egestas. Donec gravida, quam quis dictum maximus, leo erat sagittis tellus, quis posuere erat lorem vitae elit. Nunc rutrum est et commodo ornare. Donec in libero pellentesque, blandit enim non, varius lacus. Vivamus hendrerit mollis neque, vel ultricies tortor. In sed risus sem. Quisque ipsum elit, dapibus iaculis nisi eu, venenatis mollis sem. Nullam auctor dui eget aliquam vehicula.</p>
        </slot>
      </slot>
      </b-overlay>
    </b-card-body>
  </b-card>
</template>

<script>
module.exports = {
  name: "base-card",
  props: {
    collapsed: {
      type: Boolean,
      default: false
    },
    forced: {
      type: Boolean,
      default: false
    },
    max_height: {
      type: String,
      default: "600px"
    },
    over_body: {
      type: Boolean,
      default: false
    },
    scroll: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      default: "Cart title"
    },
  },
  data() {
    return { show_body: !this.collapsed };
  },
  methods: {
    header_click(event) {
      this.$emit("header_click", event)
      
      if (!this.forced) {
        this.show_body = !this.show_body;
      }
    }
  }
};
</script>

<style scoped>
</style>