# wagtail_api_test

This repo exists to point out that the output of the default Wagtail v1 API does not quite match the database contents of ListBlocks, making sync'ing ListBlocks across servers using API V2... fraught.

How to reproduce the issue at hand:

1. Publish a HomePage with at least one MixedMediaCarouselBlock that has a MixedMediablock inside it, with an image.
2. Check the database to see the dict labeled "DB contents" below.
3. Run `./manage.py runserver` and visit `http://127.0.0.1:8000/api/homepages/`.
4. You'll see that the API output transforms the JSON of the 'body' field into the "API output" dict below. 


DB contents: 
```
[
    {
        "type": "carousel",
        "value":
        {
            "items":
            [
                {
                    "type": "item",
                    "value":
                    {
                        "image": 1,
                        "video": "",
                        "caption": "test",
                        "photo_credit": "test"
                    },
                    "id": "499c302f-6230-45ed-90d4-62ecd2e845ea"
                }
            ]
        },
        "id": "5bd471ea-1fe5-4fc2-a76a-3c70897d3895"
    }
]
```

API output:
```
[
    {
        "type": "carousel",
        "value": {
            "items": [
                {
                    "image": 1,
                    "video": "",
                    "caption": "test",
                    "photo_credit": "test"
                }
            ]
        },
        "id": "5bd471ea-1fe5-4fc2-a76a-3c70897d3895"
    }
]
```

The fact that the individual MixedMediaBlocks have been stripped of their "SteamBlock-ness" -- losing their `type`, `value`, and (crucially) `id` -- makes this output difficult to use for syncing to another server, because Wagtail will be forced to recreate each ListBlock item with a newly generated ID after it's ingested into a local HomePage. 

This means the sync'd pages on both sites won't have exactly identical body fields, which will trigger ReferenceIndex changes each time that page gets sync'd, even when there aren't any differences. 
