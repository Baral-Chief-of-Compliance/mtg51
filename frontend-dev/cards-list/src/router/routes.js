const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue'), name: 'Index' },
      { path: 'wish', component: () => import('pages/WishPage.vue'), name: 'Wish'},
      { path: 'orders', component: () => import('pages/OrdersPage.vue'), name: 'Orders'},
      { path: 'useful-links', component: ()=> import('pages/UsefulLinksPage.vue'), name: 'UsefulLinks'}
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
