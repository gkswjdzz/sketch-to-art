<template>
  <div id="wrapper">
    <div class="container">
      <div class="section">
        <h3>1. Start drawing</h3>
        <div class="canvas-wrapper">
          <drawing-board ref="canvas"
                         :enabled="!userContent"></drawing-board>
        </div>
        <span id="btns">
          <button class="btn"
                @click="clearCanvas">
            <span class="clear"></span>
            <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M23.2 18H11.982L21.3656 8.61642C21.6781 8.30394 21.6781 7.79769 21.3656 7.48513L14.5149 0.634415C14.2024 0.321935 13.6962 0.321935 13.3836 0.634415L3.10744 10.9102C2.6512 11.3664 2.4 11.9727 2.4 12.618C2.4 13.2634 2.6512 13.8696 3.10744 14.3255L6.78176 18H0.8C0.35824 18 0 18.3583 0 18.8C0 19.2418 0.35824 19.6 0.8 19.6H23.2C23.6418 19.6 24 19.2418 24 18.8C24 18.3583 23.6418 18 23.2 18ZM13.9492 2.33129L19.6687 8.05082L13.3779 14.3413L7.65856 8.62193L13.9492 2.33129ZM4 12.618C4 12.4004 4.0848 12.1958 4.23864 12.0419L6.52728 9.75321L12.2466 15.4726L9.95776 17.7614C9.65072 18.0692 9.1136 18.0692 8.80584 17.7614L4.23864 13.1938C4.0848 13.0403 4 12.8355 4 12.618Z" fill="white"/>
            </svg>
            <h3>Clear</h3>
          </button>

          <form id="upload-file"
                method="post"
                enctype="multipart/form-data">
            <input type="file"
                  name="file"
                  @change="contentUpload"
                  id="imageUpload"
                  accept=".png, .jpg, .jpeg">
            <div class="btn" onclick="document.getElementById('imageUpload').click();">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.83437 14.6519V18.1664H18.1664V14.6519C18.1664 14.1453 18.5766 13.7351 19.0832 13.7351C19.5898 13.7351 20 14.1453 20 14.6519V18.2859C20.0002 19.2312 19.2312 20.0002 18.2859 20.0002H5.71453C4.76922 20.0002 3.99976 19.2312 3.99976 18.2859V14.6519C3.99976 14.1453 4.41081 13.7351 4.91707 13.7351C5.42316 13.7351 5.83437 14.1453 5.83437 14.6519Z" fill="white"/>
                <path d="M12.6485 4.26859L16.4102 8.03029C16.7684 8.3887 16.7684 8.96935 16.4102 9.32744C16.0525 9.68585 15.4716 9.68585 15.1136 9.32744L12.9478 7.16147V14.1896C12.9478 14.6961 12.5376 15.1063 12.031 15.1063C11.5244 15.1063 11.114 14.6961 11.114 14.1896V7.09986L8.88757 9.32744C8.52932 9.68585 7.94851 9.68585 7.59026 9.32744C7.41121 9.1484 7.32161 8.91335 7.32161 8.67894C7.32161 8.44454 7.41121 8.20917 7.59026 8.03013L11.3519 4.26859C11.5236 4.09643 11.7568 3.99979 12.0001 3.99979C12.2435 3.99979 12.4766 4.09643 12.6485 4.26859Z" fill="white"/>
              </svg>
              <h3 class="innerText">Upload your Drawing</h3>
            </div>
          </form>
        </span>
      </div>

      <div class="section">
        <h3>2. Choose a style!</h3>
        <div class="image-container">
          <div class="image-flex">
            <!-- div.image-item -->
            <div v-for="image in styleImages"
                 :key="image.id"
                 class="image-item">
              
              <div class="wrap">
                <image-item :src="image.src"
                            :id="image.id"
                            :selected="selectedId"
                            @clicked="onSelectStyle">
                </image-item>
                <svg v-on:click="onSelectStyle(image.id)" :id="'click-' + image.id" class='svg' width="68" height="48" viewBox="0 0 68 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 22.7342L24.8264 44L64 4" stroke="white" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <h3>{{image.name}}</h3>
            </div>
            <div class="wrap">
              <form id="upload-style"
                  method="post"
                  enctype="multipart/form-data">
                <input type="file"
                    name="file"
                    @change="styleUpload"
                    id="styleUpload"
                    accept=".png, .jpg, .jpeg">
                <div type="button" id="6"  class="svg btn" onclick="document.getElementById('styleUpload').click();">
                  <div v-if="userStyle"
                      class="upload-style">
                    <!-- <div class="remove"
                        @click="removeUserStyle">Remove</div> -->
                    <img class="btn selected" :src="userStyleSrc" @click="removeUserStyle">
                    <svg id="style-svg" class='svg' width="68" height="48" viewBox="0 0 68 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M4 22.7342L24.8264 44L64 4" stroke="white" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                  <div v-else class="innerBox">
                    <h3>+UPLOAD YOURS</h3>
                  </div>
                </div>
              </form>
              
            </div>
          </div>
        </div>

        <div class="options">
          <div class="toggle">
            <h3 v-show="highReality" class='active'>More Real</h3>
            <h3 v-show="!highReality">More Real</h3>
            <toggle-button :value="highReality"
                         :color="{checked: '#636363', unchecked: '#636363'}"
                         :switch-color="{checked: '#DFDFDF', unchecked: '#DFDFDF'}"
                         :sync="true"
                         :width="32"
                         :height="16"
                         @change="toggleReality" />
            <h3 v-show="!highReality" class='active'>More Style</h3>
            <h3 v-show="highReality">More Style</h3>
          </div>
          <div class="toggle">
            <h3 v-show="!highQuality" class='active'>High Quality</h3>
            <h3 v-show="highQuality">High Quality</h3>
            <toggle-button :value="!highQuality"
                          :color="{checked: '#636363', unchecked: '#636363'}"
                          :switch-color="{checked: '#DFDFDF', unchecked: '#DFDFDF'}"
                          :sync="true"
                          :width="32"
                          :height="16"
                          @change="toggleQuality" />
            <h3 v-show="highQuality" class='active'>High Speed</h3>
            <h3 v-show="!highQuality">High Speed</h3>
          </div>
          
          <div class="submit">
            <button v-if="!showWaitModal" class="btn"
                    :disabled="submitDisable"
                    @click="submitDrawing">
              <span>Submit!</span>
            </button>
            <button v-else id="submitBtn" class="btn" disabled>
              <div class="loader">Loading...</div>
            </button>
            <router-link to="/result"
                  id="resultId" class="route" tag=button style="display: none;">Result</router-link>
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
import ToggleButton from "vue-js-toggle-button";

Vue.use(VueSwal);
Vue.use(ToggleButton);

const axiosPix =
  process.env.NODE_ENV === "development"
    ? axios.create({ baseURL: "/" })   //FIXME : URL
    : axios.create({ baseURL: "/" });  //FIXME : URL

const axiosStyle =
  process.env.NODE_ENV === "development"
    ? axios.create({ baseURL: "/" })  //FIXME : URL
    : axios.create({ baseURL: "/" });  //FIXME : URL

export default {
  name: "LandingPage",

  components: {
    DrawingBoard,
    ImageItem
  },

  data() {
    return {
      msg: "Welcome",
      eraseImage: {
        src: require("@/assets/thumbs/Vector.png")
      },
      styleImages: [
        { id: "1", src: require("@/assets/thumbs/1.jpg"), name: "SHINKAI MAKOTO" },
        { id: "2", src: require("@/assets/thumbs/2.jpg"), name: "VAN GOGH" },
        { id: "3", src: require("@/assets/thumbs/3.jpg"), name: "CLAUDE MONET" },
        { id: "8", src: require("@/assets/thumbs/8.jpg"), name: "UKIYOE" },
        { id: "4", src: require("@/assets/thumbs/4.jpg"), name: "CARTOON" }
        // { id: "6", src: require("@/assets/thumbs/6.jpg") },
        // { id: "7", src: require("@/assets/thumbs/7.jpg") },
        // { id: "8", src: require("@/assets/thumbs/8.jpg") },
        // { id: "9", src: require("@/assets/thumbs/9.jpg") }
      ],
      selectedId: 1,
      sessionId: "",

      userContent: false,
      userStyle: false,
      userStyleSrc: "",

      highReality: true,
      highQuality: false,

      showStyle: true,
      showToggle: false,
      resultSrc: "",
      resultPix: "",
      resultStyle: "",

      showWaitModal: false,
      modalContent: "Waiting for a few seconds...",
      submitDisable: true
    };
  },

  mounted: function() {
    // this.canvasWidth = document.body.clientWidth / 2;
    // this.canvasHeight = this.canvasWidth*(3/5);
    this.selectedId = 1;
    this.sessionId =
      "_" +
      Math.random()
        .toString(36)
        .substr(2, 9);

    let that = this;
    axiosPix
      .get("/")
      .catch(function(error) {
        that.$swal({
          title: "Something wrong...",
          text:
            "Server not responding, check your Internet connection first. You can view details in the About page. To experience the app, please contact the author for help.",
          icon: "warning",
          buttons: {
            cancel: "Got it"
          }
        });
      })
      .then(response => {
        return axiosStyle.get("/");
      })
      .catch(function(error) {
      })
      .then(response => {
      });
  },

  methods: {
    clearCanvas() {
      this.$refs.canvas.clearCanvas();
      this.userContent = false;
    },

    onSelectStyle(id) {
      const svgs = document.getElementsByClassName('svg');
      const target = document.getElementById(`click-${id}`);

      this.userStyle = false;

      for (let i = 0; i < svgs.length; i++) {
        const svg = svgs[i];
        svg.classList.remove('selected');
      }
      if (target) {
        target.classList.add('selected');
      }

      this.selectedId = id;
      this.submitDisable = false;
    },

    submitDrawing() {
      // setTimeout(() => {
      //   const result = document.getElementById('resultId');
      //   result.click();
            // }, 5000);
      // Retreive canvas drawing
      var canvas = document.querySelector("#canvas");
      var context = canvas.getContext("2d");

      var w = canvas.width;
      var h = canvas.height;
      var compositeOperation = context.globalCompositeOperation;
      context.globalCompositeOperation = "destination-over";
      context.fillStyle = "white";
      context.fillRect(0, 0, w, h);

      var src = canvas.toDataURL("image/png");
      // Build form data
      var pixData = new FormData();
      var styleData = new FormData();
      pixData.append("id", this.sessionId);
      pixData.append("image", src);

      styleData.append("id", this.sessionId);
      styleData.append("style", this.selectedId);
      styleData.append("highReality", this.highReality);
      styleData.append("highQuality", this.highQuality);
      styleData.append("userContent", this.userContent);
      styleData.append("userStyle", this.userStyle);
      styleData.append("contentData", src);
      styleData.append("styleData", this.userStyleSrc);

      // Use custom image
      if (this.userContent) {
        this.modalContent = "Stylizing your picture...";
        this.showWaitModal = true;

        axiosStyle({
          url: "/stylize-with-data",
          method: "POST",
          data: styleData,
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }).then(response => {
          this.showWaitModal = false;
          this.resultStyle = response.data;
          this.resultSrc = this.resultStyle;
          this.showToggle = false;

          localStorage.setItem('user-canvas', JSON.stringify(src));
          localStorage.setItem('style-img', JSON.stringify(this.userStyleSrc));
          localStorage.setItem('styleId', this.selectedId)
          localStorage.setItem("resultSrc", JSON.stringify(this.resultSrc));
          document.getElementById('resultId').click();
        });
      } else {
        // Use sketch
        this.modalContent = "Waiting for a few seconds...";
        this.showWaitModal = true;

        axiosPix({
          url: "/pix-translate-data",
          method: "POST",
          data: pixData,
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
          .then(response => {
            this.resultPix = response.data;
            this.resultSrc = this.resultPix;
            this.modalContent = "Styling the picture...";
            return axiosStyle({
              url: "/stylize-with-data",
              method: "POST",
              data: styleData,
              headers: {
                "Content-Type": "multipart/form-data"
              }
            });
          })
          .then(response => {
            this.showWaitModal = false;
            this.resultStyle = response.data;
            this.resultSrc = this.resultStyle;
            this.showToggle = true;

            let idx = 0;
            for (let i = 0; i < this.styleImages.length; i++) {
              const styleImage = this.styleImages[i]
              if (styleImage.id === this.selectedId)
                idx = i;
            }
            localStorage.setItem('user-canvas', JSON.stringify(src));
            localStorage.setItem('style-img', JSON.stringify(this.styleImages[idx].src));
            localStorage.setItem('styleId', this.selectedId)
            localStorage.setItem("resultSrc", JSON.stringify(this.resultSrc));
            document.getElementById('resultId').click();
          });
      }
    },

    toggleReality() {
      this.highReality = !this.highReality;
    },

    toggleQuality() {
      this.highQuality = !this.highQuality;
    },

    toggleResult() {
      this.showStyle = !this.showStyle;
      if (this.showStyle) {
        this.resultSrc = this.resultStyle;
      } else {
        this.resultSrc = this.resultPix;
      }
    },

    uploadToGallery() {
      this.$swal({
        text: "Save your work to public gallery?",
        buttons: true
      }).then(willUpload => {
        if (willUpload) {
          var uploadData = new FormData();
          uploadData.append("id", this.sessionId);
          // Display overlay
          this.modalContent = "Saving...";
          this.showWaitModal = true;

          axiosStyle({
            url: "/submit-to-gallery", 
            method: "POST",
            data: uploadData,
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
            .then(response => {
              this.showWaitModal = false;
              this.$swal("Go to the gallery and check it out!", {
                icon: "success"
              });
            })
            .catch(function(response) {
              this.modalContent = "Ooops, something wrong...";
              setTimeout(function() {
                this.showWaitModal = false;
              }, 3000);
            });
        }
      });
    },

    contentUpload(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;

      var reader = new FileReader();

      reader.onload = e => {
        var canvas = document.querySelector("#canvas");
        var ctx = canvas.getContext("2d");

        var w = canvas.width;
        var h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        var img = new Image();
        img.onload = function() {
          ctx.drawImage(img, 0, 0, w, h);
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(files[0]);
      e.target.value = "";
      this.userContent = true;
    },

    styleUpload(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;

      const images = document.getElementsByClassName('selected');
      const svgs = document.getElementsByClassName('svg selected');
      
      for(let i = 0; i < images.length; i++) {
        const image = images[i];
        image.classList.remove('selected');
      }

      for(let i = 0; i < svgs.length; i++) {
        const svg = svgs[i];
        svg.classList.remove('selected');
      }

      const style_svg = document.getElementById('style-svg');
      if (style_svg) {
        style_svg.classList.add('selected');
      }

      var reader = new FileReader();
      var vm = this;

      reader.onload = e => {
        var canvas = document.createElement("canvas");
        var ctx = canvas.getContext("2d");
        var imgSize = 256;
        var image = new Image();

        canvas.width = imgSize;
        canvas.height = imgSize;

        var imgData;

        image.onload = function() {
          ctx.drawImage(image, 0, 0, imgSize, imgSize);
          let imgData = canvas.toDataURL("image/png");
          vm.setUserStyleSrc(imgData);
        };
        image.src = e.target.result;
      };
      reader.readAsDataURL(files[0]);
      e.target.value = "";
    },

    setUserStyleSrc(data) {
      this.userStyleSrc = data;
      this.userStyle = true;
      this.submitDisable = false;

      var submit = this.$el.querySelector(".submit");
      submit.scrollIntoView({ behavior: "smooth" });
    },

    removeUserStyle() {
      this.userStyle = false;
      this.userStyleSrc = "";
      this.submitDisable = true;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

#wrapper {
  padding-top: 48px;
  width: 800px;
  font-family: Muli;
}

.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container h3 {
  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 20px;

  text-align: center;
}

.section {
  align-content: center;
  margin: 32px;
}

#btns {
  display: flex;
  flex-direction: column;
  align-items: center;
}

#btns .btn {
  display: flex;
  flex-direction: row;
  flex: 0 1 atuo;
  align-items: center;
  justify-content: center;

  margin: 16px;

  background-color: #636363;
  border-radius: 24px;
  border: 0;
  outline: 0;

  width: 240px;

  height: 48px;

  color: #ffffff;
}

#btns .btn:hover {
  background-color: #333333;
}

#btns .btn:active {
  transform: scale(0.98);
}

#btns .btn h3 {
  display: inline-block;

  font-weight: bold;
  font-size: 16px;
  
  padding-left: 5px;

  font-style: normal;
  line-height: 20px;
}

#imageUpload {
  display: none;
}

#styleUpload {
  display: none;
}
/*
#wrapper h1 {
  margin: 1rem 0rem;
}

#wrapper h3 {
  margin-top: 0.2rem;
  margin-bottom: 0.8rem;
}

.container {
  display: flex;
}

.section {
  margin: 0.5rem 1rem;
  flex-grow: 1;
  width: 35%;
}

*/

.section .options .vue-js-switch {
  margin: 3px 16px 22px 16px;
}

.options {
  display: flex;
  flex-direction: column;
  align-content: center;
}

.options .toggle {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.options .toggle h3 {
  font-family: Montserrat;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;

  color: #636363;
}

.options .toggle h3.active {
  opacity: 0.6;
}

.options .toggle:nth-child(2) {
  width: 99%;
}

.section:nth-child(2) {
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 8px;
}

.section:nth-child(2) h3 {
  margin-bottom: 30px;
}

.image-container .image-flex {
  overflow: hidden;
  display: inline-flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.image-container .image-flex .wrap {
  position: relative;
  background-color: #414141;
  height: 160px;
  border-radius: 8px;
}

.image-container .image-item {
  top: 0;
  left: 0;
  width: 240px;
  padding-bottom: 40px;
  opacity: 1;
}

.image-container .mask {
  top: 0;
  left: 0;
  width: 260px;
  height: 160px;
  opacity: 1;
  background-color: #414141;
}

.image-container svg {
  position: absolute;
  z-index: 1;
  opacity: 0;
  top: 56px;
  left: 86px;
}

.image-container .image-item img.selected {
  transition: all ease 0.5s 0s;
  opacity: 0.44;
}

.image-container .image-item svg.selected {
  opacity: 1;
}

#style-svg {
  opacity: 1;
}
.image-container .image-item img {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  height: 160px;
}

.image-container .image-item h3 {
  padding-top: 6px;
  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  /* identical to box height, or 125% */
  color: #575757;
  text-align: center;
}

.image-flex .btn {
  z-index: -1;
  height: 160px;
  width: 240px;

  background: #C4C4C4;
  border-radius: 8px;
  border: 0;
  outline: none;

  display: flex;
  align-items: center;
  justify-content: center;
}

.image-flex .btn:active {
  transform: scale(0.98);
}

.image-flex .btn.selected {
  transition: all ease 0.5s 0s;
  opacity: 0.44;
}

.image-flex .btn .innerBox {
  padding: 0 30px;
}

.image-flex .btn h3 {
  padding: 10px 20px;
  margin: 0;
  background: #FFFFFF;
  border: 1px solid #DFDFDF;
  box-sizing: border-box;
  border-radius: 24px;
  
  font-size: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;

  align-self: center;
  
}

.submit {
  display: flex;
  justify-content: center;
  padding: 37px;
}


.submit button {
  background: #636363;
  border-radius: 24px;
  outline: none;
  border: 0;
  width: 240px;
  height: 48px;
}

.submit button:hover {
  background: #333333;
}

.submit button:active {
  transform: scale(0.98);
}
.submit button:disabled {
  background: #BDBDBD;
}

.submit #submitBtn:disabled {
  background: #333333;
}

.submit button span {
  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  /* identical to box height, or 125% */

  color: #FFFFFF;

}

.upload-style {
  background-color: #414141;
  border-radius: 8px;
}

.loader {
  top: -34px;
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 2em;
  height: 2em;
  border-radius: 50%;
  background: #ffffff;
  background: -moz-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -webkit-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -o-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -ms-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: linear-gradient(to right, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  position: relative;
  -webkit-animation: load3 1.4s infinite linear;
  animation: load3 1.4s infinite linear;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
.loader:before {
  width: 50%;
  height: 50%;
  background: #ffffff;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}
.loader:after {
  background: #333333;
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
@-webkit-keyframes load3 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes load3 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@media only screen and (max-width: 900px) {
  #wrapper {
    width: 520px;
  }

  .image-container .image-item {
    padding-top: 36px;
    padding-bottom: 0px;
  }

  .section:nth-child(2) h3 {
    margin-bottom: 0px;
  }

  .wrap:nth-child(6) {
    margin-top: 36px;
  }

  .options {
    padding-top: 48px;
  }

  div.submit {
    margin-bottom: 43px;
  }
}

@media only screen and (max-width: 400px) {
  #wrapper {
    width: 100%;
    padding-top: 0;
  }

  .image-container {
    display: flex;
    flex-direction: column;
  }
  .image-container .image-flex {
    flex-direction: column;
    flex-wrap: unset;

    align-items: center;
  }
  .image-container .image-item {
    padding-top: 36px;
    padding-bottom: 0px;
  }

  .section:nth-child(2) h3 {
    margin-bottom: 0px;
  }

  .wrap:nth-child(6) {
    margin-top: 36px;
  }

  .options {
    padding-top: 48px;
  }

  div.submit {
    margin-bottom: 43px;
  }
}
</style>
