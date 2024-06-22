<template>
  <div>
    <el-select v-model="value" placeholder="请选择">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
<!--  <textarea id="multiLineInput" rows="20" cols="120" style="resize: both; overflow: auto;"></textarea> -->
  <textarea v-model="inputText" placeholder="Enter text..."></textarea> <br/>

<!--  <button @click="saveData" id="submitButton">Submit</button>-->
  <button @click="sendText">Send</button>
  <p v-if="response">{{ response }}</p>
  </div>

</template>

<!--<template>-->
<!--  <div>-->
<!--&lt;!&ndash;    <textarea v-model="inputText" placeholder="Enter text..."></textarea>&ndash;&gt;-->
<!--    <button @click="sendText">Send</button>-->
<!--    <p v-if="response">{{ response }}</p>-->
<!--  </div>-->
<!--</template>-->


<!--<script>-->

<!--import dynamicRouters from '@/router/dynamic'-->
<!--import FileSaver from 'file-saver'-->
<!--import { ref } from 'vue';-->
<!--import fs from 'fs';-->
<!--import path from 'path';-->
<!--import { saveAs } from 'file-saver';-->
<!--import axios from 'axios';-->



<!--  methods: {-->
<!--    exportRouters() {-->
<!--      const jsonStr = JSON.stringify(dynamicRouters)-->
<!--      const blob = new Blob([jsonStr], { type: "text/json" })-->
<!--      FileSaver.saveAs(blob, '系统路由表.json')-->
<!--    },-->
<!--    saveData() {-->
<!--      console.log('12');-->
<!--      const multiLineInput = document.getElementById('multiLineInput');-->
<!--      const content = multiLineInput.value;-->
<!--      const fileName = 'test.cpp';-->
<!--      const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });-->
<!--      const url = URL.createObjectURL(blob);-->
<!--      const a = document.createElement("a");-->
<!--      a.href = url;-->
<!--      a.download = "hello.txt";-->
<!--      a.click();-->
<!--      URL.revokeObjectURL(url);-->
<!--      // const formData = new FormData();-->
<!--      // formData.append('file', blob, fileName);-->
<!--      // try {-->
<!--      //   const response = axios.post('/api/saveData', formData);-->
<!--      //   console.log('文件已成功保存到服务器');-->
<!--      // } catch (error) {-->
<!--      //   console.error('保存文件到服务器失败：', error);-->
<!--      // }-->
<!--    }-->
<!--  }-->
<!--}-->

<!--</script>-->


<script lang="ts">
// import { Vue, Ref } from 'vue';
//
// @Component
// export default class TextInput extends Vue {
//   inputText: string = '';
//   response: string | null = null;
//
//   async sendText(): Promise<void> {
//     try {
//       const response = await fetch('http://127.0.0.1:5000', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ text: this.inputText }),
//       });
//       const responseData = await response.json();
//       this.response = responseData.message; // 根据后端返回的数据结构来处理
//     } catch (error) {
//       console.error('Error sending text:', error);
//       this.response = 'Error sending text.';
//     }
//   }
// }



// import { defineComponent } from 'vue';
//
// export default defineComponent({
//   data() {
//     return {
//       inputText: '',
//       response: null,
//     };
//   },
//   methods: {
//     async sendText() {
//       try {
//         const response = await fetch('http://127.0.0.1:5000', {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'application/json',
//           },
//           body: JSON.stringify({ text: this.inputText }),
//         });
//         const responseData = await response.json();
//         this.response = responseData.message;
//       } catch (error) {
//         console.error('Error sending text:', error);
//         this.response = 'Error sending text.';
//       }
//     },
//   },
// });


import { defineComponent } from 'vue';
import { ElSelect, ElOption } from 'element-plus'; // 如果使用 element-plus
// import { Select, Option } from 'element-ui'; // 如果使用 element-ui 2.x

export default defineComponent({
  components: {
    ElSelect, // 如果使用 element-plus
    // Select, // 如果使用 element-ui 2.x
    ElOption // 如果使用 element-plus
    // Option // 如果使用 element-ui 2.x
  },
  data() {
    return {
      inputText: '',
      response: null,
      options: [{
        value: 'C++',
        label: 'C++'
      }, {
        value: 'C',
        label: 'C'
      }, {
        value: 'python',
        label: 'python'
      }, {
        value: 'java',
        label: 'java'
      }, {
        value: 'rust',
        label: 'rust'
      }],
      value: ''
    };
  },
  methods: {
    async sendText() {
      try {
        const response = await fetch('http://127.0.0.1:5000', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: this.inputText }),
        });
        const responseData = await response.json();
        this.response = responseData.message;

        // 可能需要根据返回的数据更新选项
        // this.options = responseData.options;
      } catch (error) {
        console.error('Error sending text:', error);
        this.response = 'Error sending text.';
      }
    },
  },
});


</script>

<style scoped>
/* 可选的样式 */
textarea {
  width: 100%;
  height: 100px;
  resize: vertical;
}
</style>
