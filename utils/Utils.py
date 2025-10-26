from typing import TypeVar, Type, Dict, Callable

T = TypeVar('T')


def singleton(class_: Type[T]) -> Callable[..., T]:
    instances: Dict[Type[T], T] = {}

    def getinstance(*args, **kwargs) -> object:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return getinstance
