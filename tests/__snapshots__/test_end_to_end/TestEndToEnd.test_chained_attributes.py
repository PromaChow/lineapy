import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import altair; altair.data_transformers.enable('json')",
    working_directory="dummy_linea_repo/",
    libraries=[
        Library(
            id=get_new_id(),
            name="altair",
        ),
    ],
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=15,
    end_lineno=1,
    end_col_offset=54,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=1,
                col_offset=47,
                end_lineno=1,
                end_col_offset=53,
                value="json",
            ).id,
        ).id
    ],
    function_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=1,
        col_offset=15,
        end_lineno=1,
        end_col_offset=46,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=15,
                    end_lineno=1,
                    end_col_offset=39,
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
                                end_col_offset=13,
                                library=Library(
                                    id=get_new_id(),
                                    name="altair",
                                ),
                            ).id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                value="data_transformers",
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
                    value="enable",
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="getattr",
        ).id,
    ).id,
)
