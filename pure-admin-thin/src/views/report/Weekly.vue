<template>
  <div class="box">
    <div ref="vantaRef" style="width: 100vw; height: 100vh;"></div>
    <div class="banner">
      <h1>每周报告</h1>
      <h6>
        &ensp;&ensp;MEI&ensp;&ensp;&ensp;ZHOU&ensp;&ensp;&ensp;&ensp;BAO&ensp;&ensp;&ensp;&ensp;&ensp;GAO
      </h6>
      <p>活动时间：待定</p>
      <p>组织单位：待定</p>
    </div>
  </div>
</template>

<script>
import * as THREE from "three";
import FOG from "vanta/src/vanta.fog";

export default {
  data() {
    return {};
  },
  mounted() {
    this.vantaEffect = FOG({
      el: this.$refs.vantaRef,
      THREE: THREE,
    });
    VANTA.FOG({
      el: this.$refs.vantaRef,
      /*以下为样式配置*/
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.0,
      minWidth: 200.0,
      highlightColor: 0xa577be,
      midtoneColor: 0xcd4841,
      lowlightColor: 0x473b6b,
      baseColor: 0xdfe3e1,
      blurFactor: 0.52,
      speed: 1.2,
      zoom: 0.3,
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
