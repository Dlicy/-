<script setup lang="ts">

defineOptions({
  // name 作为一种规范最好必须写上并且和路由的name保持一致
  name: "Monthlife"
});
</script>

<template>
  <div class="fullscreen-container">
    <div class="rectangle-pair">
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-1"></div>
    </div>
    <div class="rectangle-pair">
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-2"></div>
    </div>
    <div class="rectangle-pair">
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-3"></div>
    </div>
  </div>
</template>

<style>
.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 85vh;
  position: relative;
}

.rectangle-pair {
  position: relative;
  display: flex;
  justify-content: center; /* 新增的样式，使得子元素水平居中 */
  align-items: center; /* 新增的样式，使得子元素垂直居中 */
  width: 390px; /* 新增的样式，设置容器的宽度 */
  height: 750px; /* 新增的样式，设置容器的高度 */
  margin: 0 160px;
  margin-top: 500px;
}

.rectangle {
  width: 300px;
  height: 150px;
  background-color: #4da3dd;
  border-radius: 35px;
  position: absolute;
  z-index: 2;
}

.grey-rectangle {
  background: radial-gradient(circle, rgba(128, 128, 128, 1) 0%, rgba(128, 128, 128, 1) 100%);
  border-radius: 35px;
  position: absolute;
  z-index: 1;
  width: 300px;
  height: 150px;
  box-shadow: 10px 10px 25px 10px rgba(128, 128, 128, 0.6); /* 增加阴影的模糊距离、扩展距离和不透明度 */
}


.grey-rectangle-1 {
  transform: translate(0px, 0px);
}

.grey-rectangle-2 {
  transform: translate(0px, 0px);
}

.grey-rectangle-3 {
  transform: translate(0px, 0px);
}


</style>
