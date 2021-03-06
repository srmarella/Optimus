import cudf

from optimus.engines.cudf.dataframe import CUDFDataFrame


class Create:
    def __init__(self, root):
        self.root = root

    def dataframe(self, dict, cols=None, rows=None, pdf=None, n_partitions=1, *args, **kwargs):
        """
        Helper to create dataframe:
        :param cols: List of Tuple with name, data type and a flag to accept null
        :param rows: List of Tuples with the same number and types that cols
        :param pdf: a pandas dataframe
        :param n_partitions:
        :return: Dataframe
        """

        cdf = cudf.DataFrame(dict)

        df = CUDFDataFrame(cdf)
        return df
