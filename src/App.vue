<template>
  <div id="app">
    <header>
      <div class="header-wrapper">
        <div id="title">
          <router-link to="/"
                    class="route" tag=img :src="titleImage.src"></router-link>
          <router-link to="/"
                    class="route" tag=div>Sketch to Art</router-link>
        </div>
        <div class="router">
          <router-link to="/about"
                    class="route" tag=button>About</router-link>
        </div>
      </div>
    </header>

    <router-view/>

    <footer>
      <div id="footer">
        <div id="ainize" OnClick="location.href='https://ainize.ai/'" style="cursor:pointer;">
        <img :src="ainizeImage.src" style="width: 13.6px; height: 14px; padding-right: 8px"/>
        Powered by Ainize</div>
      <div id="git" OnClick="location.href='https://github.com/gkswjdzz/sketch-to-art'" style="cursor:pointer;">
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
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR');

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

.header-wrapper {
  width: 800px;
  display:flex;
  flex-direction: row;
  justify-content: space-between;
}

.router .route {
  width: 80px;
  height: 32px;

  background: #FFFFFF;
  border: 1px solid #DFDFDF;
  box-sizing: border-box;
  border-radius: 24px;

  outline: none;
  color: #979797;
}

.router .route:hover {
  color: #333333;
  border: 1px solid #333333;
}

#title {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  text-align: left;
  vertical-align: middle;

  cursor:pointer;
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


@media only screen and (max-width: 900px) {
  .header-wrapper {
    width: 520px;
  }
}

@media only screen and (max-width: 400px) {
  .header-wrapper {
    width: 240px;
  }
  .header-wrapper {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  button .route {
    margin-top: 14px;
  }
  #footer {
    flex-direction: column;
    padding: 0;
    margin: 40px 0;
  }

  footer div {
    margin: 0;
    padding: 0 0 20px 0;
  }
}

</style>
