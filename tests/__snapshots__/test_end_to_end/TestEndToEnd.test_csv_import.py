import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\nimport lineapy\n\ndf = pd.read_csv('tests/simple_data.csv')\ns = df['a'].sum()\n\nlineapy.linea_publish(s, \"Graph With CSV Import\")\n",
    working_directory="dummy_linea_repo/",
    session_name=None,
    user_name=None,
    hardware_spec=None,
    libraries=[
        Library(
            id=get_new_id(),
            name="lineapy",
            version=None,
            path=None,
        ),
        Library(
            id=get_new_id(),
            name="pandas",
            version=None,
            path=None,
        ),
    ],
)
import_1 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=19,
    library=Library(
        id=get_new_id(),
        name="pandas",
        version=None,
        path=None,
    ),
    attributes=None,
    alias="pd",
    module=None,
)
import_2 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=14,
    library=Library(
        id=get_new_id(),
        name="lineapy",
        version=None,
        path=None,
    ),
    attributes=None,
    alias=None,
    module=None,
)
literal_1 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=17,
    end_lineno=4,
    end_col_offset=40,
    value="tests/simple_data.csv",
)
literal_2 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=5,
    col_offset=7,
    end_lineno=5,
    end_col_offset=10,
    value="a",
)
argument_1 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=literal_1.id,
    value_literal=None,
)
argument_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_2.id,
    value_literal=None,
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=0,
    end_lineno=4,
    end_col_offset=41,
    arguments=[argument_1.id],
    function_name="read_csv",
    function_module=import_1.id,
    locally_defined_function_id=None,
    assigned_variable_name="df",
    value=None,
)
argument_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_1.id,
    value_literal=None,
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=5,
    col_offset=4,
    end_lineno=5,
    end_col_offset=11,
    arguments=[argument_2.id, argument_3.id],
    function_name="getitem",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=5,
    col_offset=0,
    end_lineno=5,
    end_col_offset=17,
    arguments=[],
    function_name="sum",
    function_module=call_2.id,
    locally_defined_function_id=None,
    assigned_variable_name="s",
    value=None,
)
