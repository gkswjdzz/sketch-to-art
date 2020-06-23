<template>
  <div id="wrapper">
    <div class="container">
      <div class="section">
        <div class="canvas-wrapper">
          <img id="resultId" />
        </div>

        <div class="input-wrapper">
          <div class="my-img">
            <h3 class="font">
              YOUR DRAWING
            </h3>
            <img :src="userCanvas" alt="" class="img">
          </div>
          <div  class="style-img">
            <h3 class="font" id="style-text">
            </h3>
            <img :src="userImg" alt="" class="img">
          </div>
        </div>

        <div class="button-wrapper">
          <div class="button">
            <router-link  class="btn" to="/" tag=button>Redraw</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DrawingBoard from "./DrawingBoard.vue";
import ImageItem from "./ImageItem.vue";
import axios from "axios";
import Vue from "vue";
import VueSwal from "vue-swal";

Vue.use(VueSwal);

const axiosPix =
  process.env.NODE_ENV === "development"
    ? axios.create({ baseURL: "/" })   //FIXME : URL
    : axios.create({ baseURL: "/" });  //FIXME : URL

const axiosStyle =
  process.env.NODE_ENV === "development"
    ? axios.create({ baseURL: "/" })  //FIXME : URL
    : axios.create({ baseURL: "/" });  //FIXME : URL

export default {
  name: "ResultPage",

  components: {
  },
  data() {
    return {
      eraseImage: {
        src: require("@/assets/thumbs/Vector.png")
      },
      styleImages: [
        { id: "1", src: require("@/assets/thumbs/1.jpg"), name: "SHINKAI MAKOTO" },
        { id: "2", src: require("@/assets/thumbs/2.jpg"), name: "VAN GOGH" },
        { id: "3", src: require("@/assets/thumbs/3.jpg"), name: "CLAUDE MONET" },
        { id: "4", src: require("@/assets/thumbs/4.jpg"), name: "UKIYOE" },
        { id: "5", src: require("@/assets/thumbs/5.jpg"), name: "CARTOON" },
        { id: "6", name: "YOUR STYLE" }
        // { id: "6", src: require("@/assets/thumbs/6.jpg") },
        // { id: "7", src: require("@/assets/thumbs/7.jpg") },
        // { id: "8", src: require("@/assets/thumbs/8.jpg") },
        // { id: "9", src: require("@/assets/thumbs/9.jpg") }
      ],
      styleId: '',
      resultSrc: '',
      targetImage: '',
      userCanvas: '',
      userImg: '',
    };
  },

  mounted: function() {
    document.getElementById('resultId').src = JSON.parse(localStorage.getItem('resultSrc'));
    this.styleId = localStorage.getItem('styleId');
    this.resultSrc = JSON.parse(localStorage.getItem('resultSrc'));
    console.log(this.styleId)
    for (let i = 0; i < this.styleImages.length; i++) {
      if (this.styleImages[i].id === this.styleId) {
        this.targetImage = this.styleImages[i]
      }
    }

    if (this.styleId !== 6) {
      this.userImg = this.targetImage.src;
    } else { 
      const styleImg = localStorage.getItem('style-img');
      this.userImg = styleImages.slice(1, styleImg.length - 1);
    }
    document.getElementById('style-text').innerText = this.targetImage.name;
    const userCanvas = localStorage.getItem('user-canvas')
    this.userCanvas = userCanvas.slice(1, userCanvas.length - 1); 
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

.container {
  width: 800px;
  display: flex;
  flex-direction: column;
}

.canvas-wrapper {
  padding: 64px 0;
}

.canvas-wrapper img {
  width: 800px;
  height: 560px;

  box-shadow: 0px 2px 16px rgba(0, 0, 0, 0.16);
  border-radius: 8px;
}

.input-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: center;
  text-align: center;
}

.input-wrapper h3 {
  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;

  padding-bottom: 20px;

  color: #575757;
}

.input-wrapper div {
  padding: 0 20px;
}

.input-wrapper .img {
  width: 240px;
  height: 180px;

  background: #FFFFFF;
  box-shadow: 0px 2px 16px rgba(0, 0, 0, 0.16);
  border-radius: 8px;
}

.button-wrapper {
  padding: 48px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button-wrapper .button {
  padding: 12px 0;
}

.button-wrapper .button button {
  width: 240px;
  height: 48px;

  background: #636363;
  border-radius: 24px;

  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  /* identical to box height, or 125% */

  color: #FFFFFF;

  border: 0;
  outline: none;
}

.button-wrapper .button .btn:hover {
  background: #333333;
}

.button-wrapper .button .btn:active {
  transform: scale(0.98);
}

</style>