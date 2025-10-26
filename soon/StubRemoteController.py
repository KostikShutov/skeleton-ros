import logging
from car.ControllerInterface import ControllerInterface
from utils.Utils import singleton


@singleton
class StubRemoteController(ControllerInterface):
    def __init__(self, entry: dict) -> None:
        self.entry: dict = entry

    def speed(self, speed: int) -> None:
        logging.info('Speed (speed: %s)' % speed)

    def forward(self, speed: int = None) -> None:
        logging.info('Forward (speed: %s)' % speed)

    def backward(self, speed: int = None) -> None:
        logging.info('Backward (speed: %s)' % speed)

    def stop(self, duration: float) -> None:
        logging.info('Stop (duration: %s)' % duration)

    def left(self) -> None:
        logging.info('Left')

    def straight(self) -> None:
        logging.info('Straight')

    def right(self) -> None:
        logging.info('Right')

    def turn(self, angle: int) -> None:
        logging.info('Turn (angle: %s)' % angle)

    def cameraLeft(self) -> None:
        logging.info('Camera left')

    def cameraRight(self) -> None:
        logging.info('Camera right')

    def cameraUp(self) -> None:
        logging.info('Camera up')

    def cameraDown(self) -> None:
        logging.info('Camera down')
