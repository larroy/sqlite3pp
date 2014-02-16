{
    "includes": [
        "../common.gypi",
    ],
    "targets":
    [
        {
            "target_name": "unit_test",
            "type": "executable",
            "dependencies": [
                "../sqlite3pp/sqlite3pp.gyp:sqlite3pp",
            ],
            "sources": [
                "main.cpp",
                "sqlite3pp.cpp",
            ],
            "include_dirs": [
                "..",
            ],
            "link_settings": {
                "libraries": [
                    "-lboost_unit_test_framework",
                    "-lsqlite3",
                    "-lboost_system",
                ],
            },
        },
    ],
}
