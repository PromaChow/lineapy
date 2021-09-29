import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\nassert pd.__name__ == 'pandas'",
    working_directory="dummy_linea_repo/",
    libraries=[
        Library(
            id=get_new_id(),
            name="pandas",
        ),
    ],
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=7,
    end_lineno=2,
    end_col_offset=30,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=2,
                col_offset=7,
                end_lineno=2,
                end_col_offset=18,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=ImportNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=1,
                            col_offset=0,
                            end_lineno=1,
                            end_col_offset=19,
                            library=Library(
                                id=get_new_id(),
                                name="pandas",
                            ),
                            alias="pd",
                        ).id,
                    ).id,
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=1,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            value="__name__",
                        ).id,
                    ).id,
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="getattr",
                ).id,
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=2,
                col_offset=22,
                end_lineno=2,
                end_col_offset=30,
                value="pandas",
            ).id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="eq",
    ).id,
)
