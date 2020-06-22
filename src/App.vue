<template>
  <div id="app">
    <header>
      <div id="title">
        <img :src="titleImage.src"/>
        <div>Sketch to Art</div>
      </div>
      <router-link to="/"
                   class="route" tag=button>Demo</router-link>
      <router-link to="/about"
                   class="route" tag=button>About</router-link>
    </header>

    <router-view/>
    <footer>
      <div id="footer">
        <div id="ainize">
        <img :src="ainizeImage.src" style="width: 13.6px; height: 14px; padding-right: 8px"/>
        Powered by Ainize</div>
      <div id="git">
        <img :src="gitImage.src" style="width: 14px; height: 14px; padding-right: 5.5px"/>
        Contribute on GitHub</div>
      </div>
    </footer>  
  </div>
</template>

<script>
export default {
  name: "App",
    data() {
      return {
        gitImage: {
          src: require("@/assets/thumbs/gitImage.png")
        },
        ainizeImage: {
          src: require("@/assets/thumbs/ainizeImage.png")
        },
        titleImage: {
          src: require("@/assets/thumbs/title.png")
        }
      }
    }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Muli');
@import url('https://fonts.googleapis.com/css?family=Montserrat');

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
    display: block;
}
body {
    line-height: 1;
}
ol, ul {
    list-style: none;
}
blockquote, q {
    quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
    content: '';
    content: none;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}

#app {
  background-color: #F6F9FC;
  font-family: Muli;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
}

header {
  font-family: Muli;
  font-style: normal;
  font-size: 20px;
  line-height: 20px;
}

.route {
  width: 80px;
  height: 32px;
  margin-left: 8px;
  text-align: center;
  background: #FFFFFF;
  border: 1px solid #DFDFDF;
  box-sizing: border-box;
  border-radius: 24px;
  font-weight: normal;
  font-size: 16px;
  line-height: 20px;
  color: #979797;
}

#title {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  text-align: left;
  vertical-align: middle;


  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 20px;
}

#title div {
  display: inline-block;
  vertical-align: middle;
}
#title img {
  margin-right: 16px;
}
.spacer {
  flex: 1;
}

header {
  text-align: left;
  display: flex;
}

header #title { 
  width: 442px;
}

@media only screen and (max-width: 800px) {

}

footer {
  width: 100%;
  background-color: #FFFFFF;
  display: flex;
  flex-direction: row;

  font-family: Montserrat;
  font-style: normal;
  font-weight: 600;
  font-size: 12px;
  
  line-height: 20px;
  color: #8E8E94;
}
footer #footer {
  width: 100%;
  justify-content: center;
  align-items: center;
}

footer div {
  margin: 20px;
  flex: 0 1 auto;
  display: flex;
}
</style>
