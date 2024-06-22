<template>
  <div class="box">
    <div ref="vantaRef" style="width: 100vw; height: 100vh;"></div>
    <div class="banner">
      <h1>每日报告</h1>
      <h6>
        &ensp;&ensp;MEI&ensp;&ensp;&ensp;RI&ensp;&ensp;&ensp;&ensp;BAO&ensp;&ensp;&ensp;&ensp;&ensp;GAO
      </h6>
      <p>活动时间：待定</p>
      <p>组织单位：待定</p>
    </div>
  </div>
</template>

<script>
import * as THREE from "three";
import BIRDS from "vanta/src/vanta.birds";

export default {
  data() {
    return {};
  },
  mounted() {
    this.vantaEffect = BIRDS({
      el: this.$refs.vantaRef,
      THREE: THREE,
    });
    // 修改颜色时 cells 需要全大写字母 可生效
    VANTA.BIRDS({
      el: this.$refs.vantaRef,
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.0,
      minWidth: 200.0,
      scale: 1.0,
      color1: 14381274,
      color2: 16443110,
    });
  },
  beforeDestroy() {
    if (this.vantaEffect) {
      this.vantaEffect.destroy();
    }
  },
};
</script>

<style lang="less" scoped>
.box {
  position: relative;
  .banner {
    z-index: 999;
    position: absolute;
    top: 30%;
    left: 10%;
    color: #fff;
  }
}
h1 {
  font-size: 66px;
}
p {
  margin-top: 60px;
  font-size: 18px;
}
</style>

