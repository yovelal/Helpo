from django.urls import path

from . import views

urlpatterns = [
    path("", views.adminPanel, name="adminPanel"), # View 1
    path("helpo_users", views.helpo_users, name="helpo_users"), # View 2
    path("AdminUpdateHelpoUser/<str:pk>/", views.AdminUpdateHelpoUser, name="AdminUpdateHelpoUser"),
    path("manager_users", views.manager_users, name="manager_users"), # View 3
    path("AdminUpdateManagerUser/<str:pk>/", views.AdminUpdateManagerUser, name="AdminUpdateManagerUser"),
    path("waiting_manager_users", views.waiting_manager_users, name="waiting_manager_users"),
    path("ApproveManager/<str:pk>/", views.ApproveManager, name="ApproveManager"),
    path("delete_approve_request/<str:pk>/", views.delete_approve_request, name="delete_approve_request"),
    path("changeActiveState/<str:pk>", views.changeActiveState, name="changeActiveState"),
    path("blockedUsers", views.blockedUsers, name="blockedUsers"),
    path("deleteUser/<str:pk>", views.deleteUser, name="deleteUser"),

    path("posts", views.adminPosts, name="posts"), # View 3
    path("AdminPostDetails/<str:pk>/", views.AdminPostDetails, name="AdminPostDetails"),
    path("AdminDeletePost/<str:pk>/", views.AdminDeletePost, name="AdminDeletePost"),

    path("categories", views.categories, name="categories"),
    path("editCategory/<str:pk>/", views.editCategory, name="editCategory"),
    path("deleteCategory/<str:pk>", views.deleteCategory, name="deleteCategory"),
    path("searchAssociation", views.searchAsso, name="searchAsso"),

    path("reports_posts", views.reports_posts, name="reports_posts"),
    path("reportsPostDetails/<str:pk>", views.reportsPostDetails, name="reportsPostDetails"),
    path("deletePostReports/<str:pk>", views.deletePostReports, name="deletePostReports"),
    path("deletePostReported/<str:pk>", views.deletePostReported, name="deletePostReported"),

    path("reports_users", views.reports_users, name="reports_users"),
    path("reportsUserDetails/<str:pk>", views.reportsUserDetails, name="reportsUserDetails"),
    path("deleteUserReports/<str:pk>", views.deleteUserReports, name="deleteUserReports"),
    path("blockUser/<str:pk>", views.blockUser, name="blockUser"),

    path("AllFeedbacks", views.AllFeedbacks, name="AllFeedbacks"),
    path("deleteFeedback/<str:pk>", views.deleteFeedback, name="deleteFeedback"),

    path("adminMessages", views.adminMessages, name="adminMessages"),
    path("editAdminMessage/<str:pk>/", views.editAdminMessage, name="editAdminMessage"),
    path("deleteAdminMessage/<str:pk>", views.deleteAdminMessage, name="deleteAdminMessage"),

    path("showActivityTracking/", views.showActivityTracking, name="showActivityTracking"),

    #Q&A
    path("show_questions/", views.show_questions, name="show_questions"),
    path("add_question/", views.add_question, name="add_question"),
    path("delete_question/<str:pk>", views.delete_question, name="delete_question"),
    path("edit_question/<str:pk>", views.edit_question, name="edit_question"),
]
