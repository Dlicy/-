<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
defineOptions({
  // name 作为一种规范最好必须写上并且和路由的name保持一致
  name: "Outline"
});

function goToDailyReport() {
  router.push("/report/Daily"); // 跳转到 /daily 路由
}

function goToWeeklyReport() {
  router.push("/report/Weekly"); // 跳转到 /daily 路由
}


function goToMonthlyReport() {
  router.push("/report/Monthly"); // 跳转到 /daily 路由
}
function goToSubmit() {
  router.push("/blog/blog")
}
function goToText() {
  router.push("/blog/creat_note")
}
</script>



<template>

  <div class="fullscreen-container">
    <!--用于创建一个全屏容器-->
    <div class="new-buttons-container">
      <div class="new-buttons-wrapper">
        <button class="my-btton" @click="goToSubmit">提交</button>
        <button class="my-btton" @click="goToText">大纲</button>
      </div>
    </div>

    <div class="rectangle-pair">
      <!--用于创建矩形和灰色矩形的容器-->
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-1"></div>
      <button class="my-button" @click="goToDailyReport">每日报告</button>
    </div>
    <div class="rectangle-pair">
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-2"></div>
      <button class="my-button" @click="goToWeeklyReport">每周报告</button>
    </div>
    <div class="rectangle-pair">
      <div class="rectangle"></div>
      <div class="grey-rectangle grey-rectangle-3"></div>
      <button class="my-button" @click="goToMonthlyReport">每月报告</button>
    </div>
  </div>
</template>

<style>
@import "Outline.css";
</style>
