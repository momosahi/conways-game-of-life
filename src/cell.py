class Cell:
    """Class that represents a cell in the grid. It has a current state, a future state, and a list of neighbors."""

    def __init__(self, current_state: bool = False, future_state: bool = False, neighbors: list = []) -> None:
        self.current_state = current_state
        self.future_state = future_state
        self.neighbors = [] if neighbors is None else neighbors

    def is_alive(self) -> bool:
        """whether the cell is alive or not."""
        return self.current_state

    def set_alive(self) -> None:
        """sets the cell to alive."""
        self.current_state = True

    def set_dead(self) -> None:
        """set the cell to dead."""
        self.current_state = False

    def set_future_state(self, state: bool) -> None:
        """set the future state of the cell.

        Parameters
        ----------
        state : bool
            the future state of the cell.
        """
        self.future_state = state

    def die(self) -> None:
        """make the cell die."""
        self.set_future_state(False)

    def live(self) -> None:
        """make the cell live."""
        self.set_future_state(True)

    def set_neighbors(self, neighbors: list) -> None:
        """get the neighbors of the cell.

        Parameters
        ----------
        neighbors : list
            the neighbors of the cell.
        """
        self.neighbors = neighbors

    def get_neighbors(self) -> list:
        return self.neighbors

    def get_neighbors_count(self) -> int:
        """get the number of neighbors of the cell."""
        return len(self.neighbors)

    def switch_state(self) -> None:
        self.current_state = self.future_state

    def __str__(self):
        """the string representation of the cell."""
        return "X" if self.current_state else "-"

    def compute_future_state(self) -> None:
        """compute the future state of the cell."""
        neighbors_count = 0
        for neighbors_cell in self.get_neighbors():
            if neighbors_cell.is_alive():
                neighbors_count += 1

        if self.is_alive():
            if neighbors_count < 2 or neighbors_count > 3:
                self.die()
        else:
            if neighbors_count == 3:
                self.live()
        self.switch_state()
