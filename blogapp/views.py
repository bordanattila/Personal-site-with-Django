from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "first-post",
        "title": "Hiking in the Mountains",
        "date": date(2021, 1, 21),
        "author": "John Doe",
        "image": "random.jpg",
        "excerpt": "Hiking in the mountains is a great way to get some exercise and enjoy the beautiful scenery.",
        "content": """Lorem ipsum odor amet, consectetuer adipiscing elit. Augue ridiculus molestie justo quisque, imperdiet dolor senectus varius. Rutrum dui habitant ad nascetur congue mi. Faucibus eros integer inceptos, netus nostra dui suspendisse. Taciti lectus ultricies eros magna vitae. Cubilia gravida laoreet pharetra accumsan mollis metus parturient fusce. Magna etiam ad est vulputate proin dignissim. Condimentum penatibus hac convallis ullamcorper senectus vestibulum lobortis magnis ac. Quis duis montes torquent consequat finibus pharetra praesent.

        Nunc augue nascetur scelerisque dapibus lacus volutpat netus curabitur gravida. Mus eros luctus orci nostra pellentesque adipiscing. Netus commodo velit magna fusce purus odio habitasse a. Fringilla vel lacus platea consequat, quis sagittis interdum? Quis magnis fermentum quis tellus lobortis. Cursus augue rhoncus per rhoncus suscipit.

        Ante elit dui elementum metus senectus. Dictum eros netus enim fames accumsan. Cubilia at molestie pellentesque purus fermentum; primis tincidunt elementum. Sollicitudin sollicitudin fringilla gravida nisl habitasse dapibus. Efficitur pharetra praesent posuere mauris praesent. Maecenas fermentum cursus nunc consectetur; tellus netus. Molestie elit consequat orci habitasse dictum donec.

        Vehicula integer nulla aliquam ligula aliquam senectus ridiculus. Adipiscing felis pretium porta a diam blandit. Ac nibh odio aenean vitae feugiat facilisi. Lacinia sociosqu at lacinia torquent gravida urna laoreet lectus. Et ipsum ornare class mi leo pulvinar lobortis primis interdum. Netus torquent eget donec tortor; mattis ipsum laoreet amet. Consectetur volutpat ex sapien mauris magnis sapien.

        Arcu lobortis sociosqu vestibulum, aenean at curabitur turpis hendrerit? Nisl mauris fames nibh netus habitasse pellentesque penatibus. Mus rutrum fringilla nisi per venenatis aliquet et aenean. Fusce adipiscing dui tincidunt, ridiculus ex et sed. Nulla ac metus himenaeos commodo eros dolor. Lorem imperdiet himenaeos duis facilisis ligula potenti eros nisl. Dis at magna nascetur est eros taciti torquent sed. Interdum quam penatibus tellus fusce placerat pharetra donec consectetur. Parturient consequat arcu elementum montes donec; semper at.
        """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "dragon-ball-z.jpg",
        "author": "Maximilian",
        "date": date(2022, 1, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "yogurt.jpg",
        "author": "Maximilian",
        "date": date(2023, 1, 21),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "harley_quinn.jpg",
        "author": "Maximilian",
        "date": date(2024, 1, 21),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }

]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts_page.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    selected_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post_details.html", {
        "selected": selected_post
    })