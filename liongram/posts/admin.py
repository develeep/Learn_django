from tabnanny import verbose
from django.contrib import admin

from posts.models import Post
from .models import Post, Comment
# Register your models here.
admin.site.register(Comment)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    verbose_name = '댓글'
    verbose_name_plural = "댓글"
# 어드민 커스텀


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content',
                    'created_at', 'view_count', 'writer',)
    # list_editable = ('content',)
    list_filter = ('created_at',)
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at', 'writer',)
    inlines = [CommentInline]
    actions = ['make_published', ]

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.update(content='운영 규정 위반 삭제 처리.')
            item.save()
        # queryset.update(status= 'p')

# admin.site.register(Comment)
