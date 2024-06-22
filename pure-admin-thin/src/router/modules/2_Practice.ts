// 使用动态导入语法导入一个异步组件，该组件在需要时才会被加载，而不是在页面初始化时立即加载。
// 这种方式可以提高应用程序的性能，特别是当组件较大或需要延迟加载时。
const AsyncComponent = () => import("@/layout/index.vue");

export default {
  // `path`定义了该路由配置的路径。
  // 当用户在浏览器中输入这个路径时，应用程序将导航到这个路由。
  path: "/Practice",

  // `name`定义了该路由配置的名称。
  // 这个名称可以在其他地方（如<router-link>组件或`this.$router.push`方法）用于引用这个路由。
  name: "Practice",

  // `component`定义了该路由配置使用的组件。
  // 当应用程序导航到这个路由时，这个组件将被渲染到<router-view>组件中。
  component: AsyncComponent,

  // `redirect`定义了当访问这个路由时的重定向路径。
  // 当用户访问这个路由时，应用程序将自动重定向到这个路径。
  redirect: "/Practice/Practice.vue",

  // `meta`定义了该路由配置的元数据。
  // 元数据是一些附加的信息，可以用于描述该路由的特性或特点。
  // 在这个例子中，元数据包含了是否显示链接、图标、标题和排名等信息。
  meta: {
    // 这个字段用于指定与路由相关联的图标。它可以是一个类名（用于字体图标库，如Font Awesome），也可以是一个图标文件的路径。在显示这个路由的链接时，这个图标可能会被显示出来
    icon: "icon_class_or_path",
    //这个字段指定了路由的标题。这个标题可能会被用于各种目的，例如设置网页的标题，或者在导航菜单中显示

    title: "Practice",
    //这个字段指定了路由的排名。在某些情况下，你可能需要根据路由的排名来排序路由的显示顺序。例如，你可能有一个导航菜单，其中的链接是按照路由的rank值从小到大排序的
    rank: 0
  },

  // `children`定义了该路由配置的子路由。
  // 子路由是嵌套在父路由下的路由配置，可以用于创建嵌套的页面结构。
  children: [
    {
      // 子路由的路径。
      path: "/Practice/Practice.vue",

      // 子路由的名称，可以用于在代码中引用这个子路由。
      name: "Practice",

      // 子路由使用的组件，这是一个异步组件。
      component: () => import("@/views/Practice/Practice.vue"),

      // 子路由的元数据，包含了标题和是否显示链接等信息。
      meta: {
        title: "在线练习",
      }
    }
  ]
}
