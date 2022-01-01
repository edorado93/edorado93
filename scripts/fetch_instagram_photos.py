import instaloader
import os

def fetch_recent_K_photos(K, handle, loader_instance):
    profile = instaloader.Profile.from_username(L.context, handle)
    posts = profile.get_posts()
    top_K_posts = []
    for p in posts:
        top_K_posts.append(p)
        K -= 1

        if not K:
            return top_K_posts

    return top_K_posts

if __name__ == "__main__":

    L = instaloader.Instaloader(dirname_pattern="instagram_posts\\{target}", filename_pattern="post")
    handle_to_consider = os.getenv("INSTAGRAM_PUBLIC_HANDLE")
    recent_posts = fetch_recent_K_photos(3, handle_to_consider, L)

    index = 0
    for post in recent_posts:
        L.download_post(post, target=("post_" + str(index)))
        index += 1


        