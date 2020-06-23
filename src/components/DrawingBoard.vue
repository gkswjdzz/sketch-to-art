<template>
  <div id="wrapper">
    <canvas id="canvas"
          v-on:mousedown="startPainting"
          v-on:mouseup="stopPainting"
          v-on:mousemove="onMouseMove"
          v-on:mouseleave="stopPainting"
          v-on:click="handleCanvasClick"
          v-on:contextmenu="handleContextMenu"
          v-on:
          v-on:touchstart="handleStart"
          v-on:touchend="handleEnd"
          v-on:touchcancel="handleCancel"
          v-on:touchmove="handleMove"
          :width="this.width"
          :height="this.height"></canvas>
  </div>
</template>

<script>
export default {
  props: ['enabled'],

  data: function() {
    return {
      INITIAL_COLOR: "#2c2c2c",
      CANVAS_WIDTH: 800,
      CANVAS_HEIGHT: 560,

      painting: false,
      filling: false
      // mouse: {
      //   current: {
      //     x: 0,
      //     y: 0
      //   },
      //   previous: {
      //     x: 0,
      //     y: 0
      //   },
      //   down: false
      // },
      // width: "",
      // height: "",
      // lineColor: "#000000",
      // lineWidth: 2
    };
  },

  // computed: {
  //   currentMouse: function() {
  //     var c = document.getElementById("canvas");
  //     var rect = c.getBoundingClientRect();

  //     return {
  //       x: this.mouse.current.x - rect.left,
  //       y: this.mouse.current.y - rect.top
  //     };
    // }
  // },

  methods: {
    stopPainting: function() {
      this.painting = false;
    },
    startPainting: function() {
      this.painting = true;
    },
    onMouseMove: function(event) {
      const x = event.offsetX;
      const y = event.offsetY;

      if (!this.painting) {
        this.ctx.beginPath();
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y);
        this.ctx.stroke();
      }
    },
    handleColorClick: function(event) {
      const color = event.target.style.backgroundColor;
      this.ctx.strokeStyle = color;
      this.ctx.fillStyle = color;
    },
    handleRangeChange: function(event) {
      this.ctx.lineWidth = parseInt(event.target.value);
    },
    handleModeClick: function() {
      if(this.filling === true) {
        this.filling = false;
        
      } else {
        filling = true;
        
      }
    },
    handleCanvasClick: function(){
      if(this.filling === true) {
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
      }
    },
    handleContextMenu: function() {
      event.preventDefault();
    },
    handleSaveClick: function() {
      const image = canvas.toDataURL("image/png");
      const link = document.createElement("a");
      link.href = image;
      link.download = "PaintJS[🎨]";
      link.click();
    },
    draw: function(event) {
      if (this.mouse.down && this.enabled) {
        var c = document.getElementById("canvas");
        var ctx = c.getContext("2d");
        ctx.clearRect(0, 0, this.width, this.height);
        ctx.lineCap = "round";
        ctx.lineTo(this.currentMouse.x, this.currentMouse.y);
        ctx.strokeStyle = this.lineColor;
        ctx.lineWidth = this.lineWidth;
        ctx.stroke();
      }
    },

    handleMouseDown: function(event) {
      console.log(event)
      this.mouse.down = true;
      this.mouse.current = {
        x: event.clientX,
        y: event.clientY
      };

      var c = document.getElementById("canvas");
      var ctx = c.getContext("2d");

      ctx.moveTo(this.currentMouse.x, this.currentMouse.y);
    },
    handleMouseUp: function() {
      this.mouse.down = false;
    },
    handleMouseMove: function(event) {
      this.mouse.current = {
        x: event.pageX,
        y: event.pageY
      };

      this.draw(event);
    },

    handleTouchStart: function(event) {
      event.preventDefault();

      var c = document.getElementById("canvas");
      var ctx = c.getContext("2d");
      var touch = event.touches[0];

      this.mouse.down = true;
      this.mouse.current = {
        x: touch.clientX,
        y: touch.clientY
      };
      ctx.moveTo(this.currentMouse.x, this.currentMouse.y);
    },
    handleTouchMove: function(event) {
      event.preventDefault();
      var touch = event.touches[0];
      this.mouse.current = {
        x: touch.eventX,
        y: touch.eventY
      };

      this.draw(event);
    },
    handleTouchEnd: function(event) {
      event.preventDefault();
      this.mouse.down = false;
    },

    clearCanvas: function() {
      var c = document.getElementById("canvas");
      c.width = c.width;
    }
  },

  ready: function() {
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    ctx.translate(0.5, 0.5);
    ctx.imageSmoothingEnabled = false;
  },

  mounted: function() {
    this.canvas= document.getElementById("canvas"),
    this.ctx= this.canvas.getContext("2d"),
         
    this.canvas.width= this.CANVAS_WIDTH,
    this.canvas.height= this.CANVAS_HEIGHT,

    this.ctx.fillStyle = "white";
    this.ctx.fillRect(0, 0, this.CANVAS_WIDTH, this.CANVAS_HEIGHT);

    this.ctx.strokeStyle = this.INITIAL_COLOR;
    this.ctx.fillStyle = this.INITIAL_COLOR;

    this.ctx.lineWidth = 2.5;
  }
};
</script>

<style scoped>
#wrapper {
  padding: 24px;
}
canvas {
  background: #FFFFFF;
  box-shadow: 0px 2px 16px rgba(0, 0, 0, 0.16);
  border-radius: 8px;
  cursor: crosshair;
  width: 800px;
  height: 560px;
}

@media only screen and (max-width: 900px) {
  canvas {
    width: 520px;
    height: 364px;
  }
}

@media only screen and (max-width: 400px) {
  canvas {
    width: 312px;
    height: 236px;
  }
}

</style>