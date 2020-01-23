import random


def max_heapify(arr, size, root):
    child = root * 2  # 부모로부터 왼쪽 자식 노드 찾기
    while child <= size:  # 배열의 인덱스 범위 초과되는걸 방지
        # 오른쪽 자식이 존재하고, 왼쪽 자식이 오른쪽 자식 값보다 작다면
        # 오른쪽 값이 큰 노드가 되도록 1을 더함
        if child < size and arr[child - 1] < arr[child]:
            child += 1
        # 부모와 자식 노드 값을 비교
        if arr[root - 1] < arr[child - 1]:
            arr[root - 1], arr[child - 1] = arr[child - 1], arr[root - 1]
        # 자식의 자식 노드로 이동
        root = child
        child = root * 2


def heap_sort(arr, size):
    # Make heap(역순으로 진행)
    for i in range(size // 2, 0, -1):  # 제일 마지막에 있는 노드의 부모를 찾기
        max_heapify(arr, size, i)
        print(i)
    # 정렬 과정(처음 값과 마지막 값을 교환하면서 힙 정렬)
    for i in range(size, 1, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        max_heapify(arr, i - 1, 1)
    return arr


# data_list = random.sample(range(20), 10)
data_list = [8, 5, 9, 3, 1, 6, 7, 2, 4]
print(heap_sort(data_list, len(data_list)))

"""
힙 정렬
1. 최댓값 최솟값을 찾기 위해 완전 이진 트리 구조의 기반인 정렬
2. 완전 이진 트리는 데이터가 왼쪽, 오른쪽 노드 순으로 차근차근 쌓임.
   중간에 비어있지 않고 빽빽히 가득 찬 트리 구조. 
특징
1. 배열로 만들 경우 부모 노드가 k라면 자식 노드는 2*k, 2*k+1로 구성
2. 부모 노드의 값이 자식 노드의 값보다 커야된다
3. 맨 처음 값과 맨 마지막 값을 교환하고 정렬 진행. 이후 마지막 값의 범위를
   좁혀가면서 계속 진행
"""

""" 참고 자료
1. http://blog.naver.com/PostView.nhn?blogId=dnpc7848&logNo=221431759144&parentCategoryNo=&categoryNo=6&viewDate=&isShowPopularPosts=true&from=search
2. https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/
3. https://www.youtube.com/watch?v=iyl9bfp_8ag
"""