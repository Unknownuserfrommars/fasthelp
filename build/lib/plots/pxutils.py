import plotly.express as px  # noqa: F401

class PXUtils:
    def __init__(self, graph_type: str, df, x_col, y_col, color_col, title: str, facet_col: str = None, facet_row: str = None, height: int = None, width: int = None, hover_data: list = None, other_kwargs: dict = None):
        """
        Initialize the graphing class.

        Parameters:
        graph_type (str): Type of the graph (e.g., 'scatter', 'bar').
        df: The DataFrame containing the data.
        x_col: The column for the x-axis.
        y_col: The column for the y-axis.
        color_col: The column for coloring the graph.
        title (str): Title of the graph.
        facet_col (str): The column for faceting the graph into columns.
        facet_row (str): The column for faceting the graph into rows.
        height (int): Height of the graph.
        width (int): Width of the graph.
        hover_data (list): Additional columns to display on hover.
        other_kwargs (dict): Additional keyword arguments for the graph.
        """
        self.graph_type = graph_type
        self.df = df
        self.x_col = x_col
        self.y_col = y_col
        self.color_col = color_col
        self.title = title
        self.facet_col = facet_col
        self.facet_row = facet_row
        self.height = height
        self.width = width
        self.hover_data = hover_data
        self.other_kwargs = other_kwargs or {}  # Default to empty dict if None
        self.fig = None

    def make_graph(self):
        """
        Generate the graph using Plotly Express.

        Returns:
        A Plotly figure object.
        """
        self.fig = eval(
            f"px.{self.graph_type}(self.df, x=self.x_col, y=self.y_col, color=self.color_col, title=self.title, "
            f"facet_col=self.facet_col, facet_row=self.facet_row, height=self.height, width=self.width, "
            f"hover_data=self.hover_data, **self.other_kwargs)"
        )
        return self.fig
