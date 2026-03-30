class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = Counter(tasks)
        max_freq = max(task_map.values())
        num_max = list(task_map.values()).count(max_freq)
        frame = (max_freq - 1) * (n + 1)
        calc_time = frame + num_max

        return max(calc_time, len(tasks))
