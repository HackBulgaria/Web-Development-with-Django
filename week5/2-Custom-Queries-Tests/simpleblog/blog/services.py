from .models import BlogPost, Tag


def create_blog_post(*,
                     title,
                     content,
                     tags=None):
    errors = []

    if not title.strip():
        errors.append('Title is required.')

    if not content.strip():
        errors.append('Content is required.')

    if errors:
        return None, errors

    post = BlogPost.objects.create(title=title, content=content)

    for tag in Tag.objects.filter(id__in=tags):
        post.tags.add(tag)

    post.save()

    return post, None
