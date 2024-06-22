// // import axios from 'axios';
// //
// // export default {
// //   // ...其他代码
// //   methods: {
// //     // ...其他方法
// //     sendDataToBackend(content) {
// //       axios.post('/api/saveData', { content })
// //         .then(response => {
// //           console.log('数据已成功发送到后端：', response);
// //         })
// //         .catch(error => {
// //           console.error('发送数据到后端失败：', error);
// //         });
// //     }
// //   }
// // }
//
// <template>
//   <div>
//     <el-select v-model="value" placeholder="请选择">
//       <el-option
//         v-for="item in options"
//         :key="item.value"
//         :label="item.label"
//         :value="item.value">
//       </el-option>
//     </el-select>
//   </div>
//   <textarea id="multiLineInput" rows="20" cols="120" style="resize: both; overflow: auto;"></textarea> <br/>
//
//   <button @click="saveData" id="submitButton">Submit</button>
// </template>
//
// <script>
// import { ref } from 'vue';
// import fs from 'fs';
// import path from 'path';
// import { saveAs } from 'file-saver';
// import axios from 'axios';
//
//
// export default {
//   data() {
//     return {
//       options: [{
//         value: 'c',
//         label: 'c'
//       }, {
//         value: 'c++',
//         label: 'c++'
//       }, {
//         value: 'java',
//         label: 'java'
//       }, {
//         value: 'python',
//         label: 'python'
//       }],
//       value: ''
//     }
//   },
//
// //   methods: {
// //   saveData() {
// //     console.log(12);
// //     const multiLineInput = document.getElementById('multiLineInput');
// //     const content = multiLineInput.value;
// //     const fileName = 'test.cpp';
// //     const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
// //     saveAs(blob, fileName);
// //   }
// // }
//
//   export default {
//     data() {
//       return {
//         fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}]
//       };
//     },
//     methods: {
//       handleRemove(file, fileList) {
//         console.log(file, fileList);
//       },
//       handlePreview(file) {
//         console.log(file);
//       },
//       handleExceed(files, fileList) {
//         this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
//       },
//       beforeRemove(file, fileList) {
//         return this.$confirm(`确定移除 ${ file.name }？`);
//       }
//     }
//   }
//
//   methods: {
//   saveData() {
//     console.log('12');
//     const multiLineInput = document.getElementById('multiLineInput');
//     const content = multiLineInput.value;
//     const fileName = 'test.cpp';
//     const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
//     const formData = new FormData();
//     formData.append('file', blob, fileName);
//     try {
//       const response = axios.post('/api/saveData', formData);
//       console.log('文件已成功保存到服务器');
//     } catch (error) {
//       console.error('保存文件到服务器失败：', error);
//     }
//   }
// }
//
//
// }
// </script>
