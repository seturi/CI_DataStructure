from collections import deque
from subway_graph import *

# 코드를 추가하세요
def bfs(graph, start_node):
    """최단 경로용 bfs 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)
    
    while queue:  # 큐에 노드가 있을 때까지
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                queue.append(neighbor)  # 큐에 넣는다
                neighbor.predecessor = current_station

def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""  # 리턴할 결과 문자열
    # 코드를 쓰세요
    stack = deque()
    stack.append(destination_node)
    while destination_node.predecessor is not None:
        back_track(destination_node.predecessor)
        stack.append(destination_node.predecessor)
        destination_node = destination_node.predecessor
    while stack:
        res_str += stack.pop().station_name + " "
    return res_str
    
stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["을지로3가"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["강동구청"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력
