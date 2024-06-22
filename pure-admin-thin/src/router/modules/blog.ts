import { compareTime } from "element-plus/es/components/time-select/src/utils.mjs";

const Layout = () => import("@/layout/index.vue");
// Layout 是一个异步组件，意味着它在需要时才会被加载，而不是在页面初始化时立即加载。
// 这种方式可以提高应用程序的性能，特别是当组件较大或者需要延迟加载时。
export default {
  path: "/blog",
  name: "Blog",
  component: Layout,
  redirect: "/blog/blog",
  
  meta: {
    showLink: false,
    icon: "material-symbols-light:bookmark",
    // 这个属性指定了一个图标，使用了一个特定的图标字体集合（例如 Material Design）。
    // 这里的图标表示为 "material-symbols-light:bookmark"，它可能会根据你的项目和图标字体库的设置而有所不同。
    title: "云课堂",
    rank: 0
  },
  children: [
    {
      path: "/blog/blog",
      name: "BlogPage",
      component: () => import("@/views/blog/blog.vue"),
      meta: {
        title: "上传文件",
        showLink: true
      }
    },
    //第二个子目录

    {
      path: "/blog/creat_note",
      name: "Class_Note",
      component: () => import("@/views/blog/create_note.vue"),
      meta: {
        title: "生成大纲",
        showLink: true
      }
    },

    // 三级目录
    {
      path: "/blog/day/day",
      meta: {
        title: "学习报"
      },

      children: [
        {
          path: "/blog/day/day",
          component: () => import("@/views/blog/day/day.vue"),
          name: "Daylife",
          meta: {
            title: "每日学习报告"
          }
        },
        {
          path: "/blog/day/week",
          component: () => import("@/views/blog/day/week.vue"),
          name: "Weeklife",
          meta: {
            title: "每周学习报告"
          }
        },
        {
          path: "/blog/day/month",
          component: () => import("@/views/blog/day/month.vue"),
          name: "Monthlife",
          meta: {
            title: "每月学习报告"
          }
        }
      ]
    }
  ]
} satisfies RouteConfigsTable;
