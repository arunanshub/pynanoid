from Cython.Build import cythonize  # type: ignore[import-untyped]


def pdm_build_update_setup_kwargs(_context, setup_kwargs):
    setup_kwargs.update(
        ext_modules=cythonize(
            "src/**/*.pyx",
            compiler_directives={"language_level": "3"},
        ),
    )
