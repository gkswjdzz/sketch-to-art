<template>
  <div id="wrapper">
    <canvas id="canvas"
          v-on:mousedown="startPainting"
          v-on:mouseup="stopPainting"
          v-on:mousemove="onMouseMove"
          v-on:mouseleave="stopPainting"

          v-on:touchstart="handleStart"
          v-on:touchend="stopPainting"
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
      CANVAS_WIDTH: '',
      CANVAS_HEIGHT: '',

      painting: false,
      filling: false,
      vw: 0,
      vh: 0
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
    handleStart: function(evt) {
      console.log('start');
      this.painting = true;
      this.ctx.beginPath();
      this.ctx.moveTo(x, y);
    },
    handleEnd: function() {

    },
    handleCancel: function() {
      
    },
    handleMove: function(e) {
      e.preventDefault();
      const rect = e.target.getBoundingClientRect();
      const x = e.touches[0].pageX - e.touches[0].target.offsetLeft;
      const y = e.touches[0].pageY - e.touches[0].target.offsetTop;
      
      if (!this.painting) {
        this.ctx.beginPath();
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y);
        this.ctx.stroke();
      }
    },
    stopPainting: function() {
      console.log('stop');
      this.painting = false;
    },
    startPainting: function() {
      console.log('start');
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
    this.canvas = document.getElementById("canvas"),
    this.ctx = this.canvas.getContext("2d"),
         
    this.vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
    this.vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
    
    if (this.vw > 900) {
      this.CANVAS_WIDTH = 800;
      this.CANVAS_HEIGHT = 560;
    } else if (this.vw > 400) {
      this.CANVAS_WIDTH = 520;
      this.CANVAS_HEIGHT = 364;
    } else {
      this.CANVAS_WIDTH = 312;
      this.CANVAS_HEIGHT = 236;
    }

    this.canvas.width= this.CANVAS_WIDTH,
    this.canvas.height= this.CANVAS_HEIGHT,

    console.log(this.canvas.width, this.canvas.height);

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