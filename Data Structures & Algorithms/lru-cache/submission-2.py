class LRUCache:
    def __init__(self, capacity: int):
        self.data={}
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key in self.data:
            val=self.data.pop(key)
            self.data[key]=val
            return  val
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            val=self.data.pop(key)
            self.data[key]=value
            return

        if len(self.data)>=self.capacity:
            for i in self.data.keys():
                old_key=i
                break
            self.data.pop(old_key)
        self.data[key]=value

        