import reddit
import asyncio
import random
from utils.config import basicconfig


async def fetch_random_meme(subreddit_name="Funnymemes", mode="hot", limit=50):
    """
    Fetches a random meme post with an image from a specified subreddit.
    This asynchronous function retrieves posts from a given subreddit and selects a random post that contains an image.
    It supports specifying the subreddit, the sorting mode, and the number of posts to consider.
    Parameters:
        subreddit_name (str): The name of the subreddit to fetch memes from. Defaults to "Funnymemes".
        mode (str): The sorting mode for subreddit posts (e.g., "hot", "new", "top"). Defaults to "hot".
        limit (int): The maximum number of posts to fetch and search for images. Defaults to 50.
    Returns:
        dict or None: A dictionary containing the following keys if a meme with an image is found:
            - "title" (str): The title of the Reddit post.
            - "image_url" (str): The direct URL to the image.
            - "permalink" (str): The permalink to the Reddit post.
        Returns None if no image posts are found within the specified limit.
    Raises:
        KeyError: If an image is not found at a specific index (handled internally).
        Exception: Propagates any exceptions raised by the underlying Reddit client.
    """
    client = reddit.AsyncClient(basicconfig.USER_AGENT, basicconfig.CLIENT_SECRET)
    
    subreddit = await client.Subreddit(mode, subreddit_name, limit=limit)
    
    image_indices = []
    for idx in range(limit):
        try:
            await subreddit.image(idx)
            image_indices.append(idx)
        except KeyError:
            continue
    
    if not image_indices:
        return None

    idx = random.choice(image_indices)
    title = await subreddit.title(idx)
    image_url = await subreddit.image(idx)
    permalink = await subreddit.permalink(idx)
    author = await subreddit.author(idx)

    return {
        "title": title,
        "image_url": image_url,
        "permalink": f"https://reddit.com{permalink}",
        "author": author
    }