from django.shortcuts import render
import aiohttp
import asyncio


def index(request):
    if request.method == 'GET':
        try:
            url = request.GET.get('text')
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            list_info = loop.run_until_complete(foo(url))

            return render(request, 'Kit/index.html', {'list_info': list_info})
        except:
            return render(request, 'Kit/index.html', {'message': 'Error'})


async def foo(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                list_info = await resp.json()
                return list_info
    except:
        return None