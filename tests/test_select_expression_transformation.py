from spark_fast_etl.transformation.transformation import (
    CommonTransformationConfig,
    SelectExpressionTransformation,
)
from spark_fast_etl.utils.SparkUtils import SparkUtils


def test_select_expression_transformation():
    spark_utils = SparkUtils()
    dummy_df = spark_utils.load_local_json("test_files/dummy_df_1.json")
    sel_expr_config = CommonTransformationConfig("awesome config")
    sel_expr_trans = SelectExpressionTransformation()

    sel_expr_trans.transform(dummy_df, sel_expr_config).show()

    # TODO finish checks
    assert 1 == 1
