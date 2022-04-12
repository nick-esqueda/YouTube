```
const state = {
    
    session: {
        id: 1,
        channelName: "Example 1",
        profileImageUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
        about: "This is an example description/about section"
        email: "example@example.com",
        createdAt: <timestamp>
    },
    
    videos: {
        1: {
            id: 1,
            channelId: 1,
            title: "example",
            description: "example",
            videoUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
            thumbnailUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
            createdAt: <timestamp>
            views: <number of views calculated by backend a query of the "Views" table>
            videoLikes: [
                {
                    id: 1
                    videoId: 1,
                    channelId: 2,
                    isLike: true
                },
                {
                    ...
                },
            ],
            comments: [
                {
                    id: 1,
                    videoId: 1,
                    channelId: 2,
                    content: "This is the content for comment 1",
                    commentLikes: [
                        {
                            id: 1
                            videoId: 1,
                            channelId: 2,
                            isLike: true
                        },
                        {
                            ...
                        },
                    ],
                },
                {
                    ...
                }
            ]
        },
        2: {
            ...
        },
        
    channels: {
        1: {
            id: 1,
            channelName: "Example 1",
            profileImageUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
            about: "This is an example description/about section"
            email: "example@example.com",
            createdAt: [timestamp],
            videos: [
                {
                    id: 1,
                    channelId: 1,
                    title: "example",
                    description: "example",
                    videoUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
                    thumbnailUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
                    createdAt: <timestamp>
                    views: <number of views calculated by backend a query of the "Views" table>
                    videoLikes: [
                        {
                            id: 1
                            videoId: 1,
                            channelId: 2,
                            isLike: true
                        },
                        {
                            ...
                        },
                    ],
                    comments: [
                        {
                            id: 1,
                            videoId: 1,
                            channelId: 2,
                            content: "This is the content for comment 1",
                        },
                        {
                            ...
                        }
                    ]
                },
                {
                    ...
                },        
            ],
            subscribers: [
                {
                    id: 2,
                    channelName: "Example 2",
                    profileImageUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
                    about: "This user (channel) is subscribed to 'Example 1's channel"
                    email: "example@example.com",
                    createdAt: [timestamp] 
                },
                {
                    ...
                },
            ], 
            subscriptions: [
                {
                    id: 3,
                    channelName: "Example 3",
                    profileImageUrl: 'https://example-bucket.s3.amazonaws.com/example.png',
                    about: "User (channel) 'Example 1' is subscribed to this channel"
                    email: "example@example.com",
                    createdAt: [timestamp] 
                },
                {
                    ...
                },
            ], 
        },
        2: {
            ...
        }
    },
    
    search: {
        videos: [...]
        channels: [...]
    }
}
```
