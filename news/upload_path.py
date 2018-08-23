#upload path for each picture,i dont know how to break my codes so i repeat

def post_image(instance, filename):
    return "%s/%s" % (instance.slug, filename)

