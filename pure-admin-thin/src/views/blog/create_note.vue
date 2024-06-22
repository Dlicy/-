<!--<template>-->
<!--  <div class="outline-container">-->
<!--    <div class="outline-sidebar">-->
<!--      <table>-->
<!--        <thead>-->
<!--          <tr>-->
<!--            <th>日期</th>-->
<!--            <th>选择</th>-->
<!--          </tr>-->
<!--        </thead>-->
<!--        <tbody>-->
<!--          <tr-->
<!--            v-for="(outline, index) in outlines"-->
<!--            :key="index"-->
<!--            @click="selectOutline(outline)"-->
<!--          >-->
<!--            <td>{{ outline.date }}</td>-->
<!--            <td><input v-model="outline.selected" type="checkbox" /></td>-->
<!--          </tr>-->
<!--        </tbody>-->
<!--      </table>-->
<!--    </div>-->
<!--    <div class="outline-content">-->
<!--      <h2>所选大纲内容</h2>-->
<!--      <div v-if="selectedOutline">-->
<!--        <h3>{{ selectedOutline.date }}</h3>-->
<!--        <p>{{ selectedOutline.description }}</p>-->
<!--        <ul>-->
<!--          <li v-for="(item, itemIndex) in selectedOutline.items" :key="itemIndex">-->
<!--            {{ item }}-->
<!--          </li>-->
<!--        </ul>-->
<!--      </div>-->
<!--      <div v-else>-->
<!--        <p>请选择一个大纲来查看内容。</p>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { ref, watch } from "vue";-->
<!--import { useFileReader } from "./useFileReader.js";-->

<!--export default {-->
<!--  name: "OutlinePage",-->
<!--  setup() {-->
<!--    const outlines = ref([-->
<!--      {-->
<!--        date: "2023-04-01",-->
<!--        items: ["项目 1", "项目 2", "项目 3"],-->
<!--        selected: false,-->
<!--        description: ""-->
<!--      },-->
<!--      {-->
<!--        date: "2023-04-02",-->
<!--        items: ["项目 A", "项目 B", "项目 C"],-->
<!--        selected: false,-->
<!--        description: ""-->
<!--      }-->
<!--    ]);-->
<!--    const selectedOutline = ref(null);-->
<!--    const { fileContent, readFile } = useFileReader();-->

<!--    function selectOutline(outline) {-->
<!--      // 取消其他大纲的选中状态-->
<!--      outlines.value.forEach(o => (o.selected = false));-->
<!--      outline.selected = true;-->
<!--      selectedOutline.value = outline;-->
<!--      readFile("text.txt"); // 读取 text.txt 文件-->
<!--    }-->

<!--    watch(fileContent, content => {-->
<!--      // 将文件内容设置到选中大纲的 description 属性-->
<!--      if (selectedOutline.value) {-->
<!--        selectedOutline.value.description = content;-->
<!--      }-->
<!--    });-->

<!--    return { outlines, selectedOutline, selectOutline, fileContent };-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.outline-container {-->
<!--  display: flex;-->
<!--}-->

<!--.outline-sidebar {-->
<!--  width: 30%;-->
<!--  padding: 10px;-->
<!--  border-right: 1px solid #ddd;-->
<!--}-->

<!--.outline-content {-->
<!--  width: 70%;-->
<!--  padding: 10px;-->
<!--}-->
<!--</style>-->










<!--<template>-->
<!--  <div class="hello">-->
<!--    <h1>This is a show file page</h1>-->
<!--    <h3>导入文件：<input type="file" name="file" @change="showFile($event)" /> </h3><br>-->
<!--    <textarea v-model="input_text" name="" cols="100" rows="20" placeholder="输入……"></textarea><br><br>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--  export default {-->
<!--    name: "Hello",-->
<!--    data: function() {-->
<!--      return {-->
<!--        input_text: ''-->
<!--      }-->
<!--    },-->
<!--    methods: {-->

<!--      showFile(input) {-->
<!--        //支持chrome IE10-->
<!--        if (window.FileReader) {-->
<!--          var file = input.target.files[0];-->
<!--          var reader = new FileReader();-->
<!--          reader.onload=((event)=>{-->
<!--            //显示文件-->
<!--            this.input_text=event.target.result;-->
<!--            console.log(event.target.result)-->
<!--          })-->
<!--          console.info(file)-->
<!--          console.info(reader);-->
<!--          reader.readAsText(file);-->
<!--        }-->
<!--        else {-->
<!--          alert("FileReader Not supported by your browser!");-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--</script>-->


<!--&lt;!&ndash; Add "scoped" attribute to limit CSS to this component only &ndash;&gt;-->
<!--<style scoped>-->
<!--  h3 {-->
<!--    margin: 40px 0 0;-->
<!--  }-->
<!--  ul {-->
<!--    list-style-type: none;-->
<!--    padding: 0;-->
<!--  }-->
<!--  li {-->
<!--    display: inline-block;-->
<!--    margin: 0 10px;-->
<!--  }-->
<!--  a {-->
<!--    color: #42b983;-->
<!--  }-->
<!--</style>-->



<template>
  <div>
    <h1>读取的文本内容：</h1>
    <p>{{ fileContent }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileContent: '' // 初始化文本内容为空字符串
    };
  },
  mounted() {
    this.readFile(); // 组件挂载后读取文件
  },
  methods: {
    readFile() {
      fetch('src/views/blog/text.txt') // 假设文件路径正确
        .then(response => response.text()) // 读取响应内容为文本
        .then(data => {
          this.fileContent = data; // 将读取到的文本内容赋值给响应式属性
        })
        .catch(error => {
          console.error('读取文件时发生错误:', error);
        });
    }
  }
};
</script>
