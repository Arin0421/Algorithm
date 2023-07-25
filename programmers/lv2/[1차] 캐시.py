def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for city in cities:
        city=city.lower()
    
        if cacheSize:
            if city not in cache:
                if len(cache)==cacheSize:
                    cache.pop(0)
                answer+=5
                cache.append(city)
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer+=1
        else:
            answer+=5
    return answer
