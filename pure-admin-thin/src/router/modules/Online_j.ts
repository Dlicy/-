const Layout = () => import("@/layout/index.vue");
// Layout 是一个异步组件，意味着它在需要时才会被加载，而不是在页面初始化时立即加载。
// 这种方式可以提高应用程序的性能，特别是当组件较大或者需要延迟加载时。

//这行代码定义了一个名为 Layout 的变量，它是一个异步组件。
//异步组件表示在需要时才会被加载，而不是在页面初始化时立即加载。
//此处的 Layout 组件被导入自 @/layout/index.vue 的路径。
export default {
  // . 这是一个导出默认对象的语法，整个对象定义了一个路由配置。
  //这个对象将被导出，以便在其他地方可以导入和使用这个路由配置。

  path: "/online_judge",

  //这行代码指定了该路由配置的路径为 /ai_dxl，表示该路由对应的路径是 /ai_dxl。
  name: "OJ",

  //这行代码指定了该路由配置的名称为 "AI_dxl"，可以通过该名称在代码中引用该路由。
  component: Layout,

  //这行代码指定了该路由配置使用的组件是之前定义的 Layout 组件。
  redirect: "/online_judge/online_judge",


  meta: {
    //这行代码定义了该路由配置的元数据（metadata）。
    //元数据是一些附加的信息，用于描述该路由的特性或特点。
    //在这个例子中，元数据包含了图标、标题和排名等信息。
    showLink: false,
    icon: "material-symbols-light:bookmark",
    title: "Online Judge 社区",
    rank: 0
  },
  children: [
    //这行代码定义了该路由配置的子路由。
    //子路由是嵌套在父路由下的路由配置，用于创建嵌套的页面结构。

    {
      path: "/online_judge/online_judge",
      //这行代码指定了子路由的路径为 /ai_dxl/ai_dxl。
      name: "OJ_S",
      //这行代码指定了子路由的名称为 "dxl"。
      component: () => import("@/views/online_judge/online_judge.vue"),
      //这行代码指定了子路由使用的组件。
      //该组件是一个异步组件，通过动态导入的方式引入自 @/views/ai_dxl / ai_dxl.vue 的路径。
      meta: {
        //这行代码定义了子路由的元数据。在这个例子中，元数据包含了标题和 showLink 属性。
        title: "OJ首页",
        showLink: true
      }
    }
  ]
} satisfies RouteConfigsTable;
