from abc import ABC, abstractmethod

class ObservableInterface(ABC):

    def __init__(self) -> None:
        self.observers = []

    @abstractmethod
    def add_observer(self, observer):
        pass
        
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    def notify(self):
        pass

    def set_data(self):
        pass

class ConcereteObservable(ObservableInterface):

    def add_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify(self):
        for each_observer in self.observers:
            each_observer.update()

    def set_data(self):
        pass

    def get_data(self):
        pass

class ObservableInterface(ABC):

    @abstractmethod
    def update(self):
        pass

class ObservableConcreteClass(ObservableInterface):

    def __init__(self, observable) -> None:
        self.observable = observable

    def update(self):
        print("Notification has been sent")

observable = ConcereteObservable()
obj1 = ObservableConcreteClass(observable)
obj2 = ObservableConcreteClass(observable)
obj3 = ObservableConcreteClass(observable)

observable.add_observer(obj1)
observable.add_observer(obj2)
observable.add_observer(obj3)
observable.remove_observer(obj1)

observable.notify()
print("No of observers currently ",len(observable.observers))
