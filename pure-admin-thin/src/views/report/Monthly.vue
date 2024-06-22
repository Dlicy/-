<template>
  <div class="box">
    <div ref="vantaRef" style="width: 100vw; height: 100vh;"></div>
    <div class="banner">
      <h1>每月报告</h1>
      <h6>
        &ensp;&ensp;MEI&ensp;&ensp;&ensp;YUE&ensp;&ensp;&ensp;&ensp;BAO&ensp;&ensp;&ensp;&ensp;&ensp;GAO
      </h6>
      <p>活动时间：待定</p>
      <p>组织单位：待定</p>
    </div>
  </div>
</template>

<script>
import * as THREE from "three";
import WAVES from "vanta/src/vanta.waves";

export default {
  data() {
    return {};
  },
  mounted() {
    this.vantaEffect = WAVES({
      el: this.$refs.vantaRef,
      THREE: THREE,
    });
    VANTA.WAVES({
      el: this.$refs.vantaRef,
      /*以下为样式配置*/
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.0,
      minWidth: 200.0,
      scale: 1.0,
      scaleMobile: 1.0,
      color: 0x5f88,
      shininess: 76.0,
      waveHeight: 12.0,
      waveSpeed: 0.95,
      zoom: 0.89,
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
