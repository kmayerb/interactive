import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _(cnames_ui, mo):
    # Extract values from the input widgets
    adjective = cnames_ui["adjective"].value
    person = cnames_ui["person"].value
    greeting = f"Hello {adjective} {person}"
    mo.md(
    f"""
    ### {greeting}
    """
    )
    return greeting

@app.cell
def _(mo):
    cnames_ui = mo.md("""
    {adjective}
    {person}        
    """).batch(
        adjective=mo.ui.text(
            label="",
            value="Curious"
        ),
        person=mo.ui.dropdown(
            label="",
            options=[
                "J.Salk",
                "L.Pauling",
                "M.Curie",        # Marie Curie
                "A.Einstein",
                "R.Franklin",     # Rosalind Franklin
                "C.Darwin",
                "B.Franklin",
                "K.Johnson",      # Katherine Johnson
                "J.Goodall",      # Jane Goodall
                "L.Meitner",      # Lise Meitner
                "N.Tesla",
                "G.Hopper"        # Grace Hopper
            ],
            value="J.Salk"
        )
    )
    cnames_ui
    return (cnames_ui,)


# @app.cell
# def _(mo):
#     import pandas as pd
#     import matplotlib.pyplot as plt

#     # Load the penguins dataset
#     fp = str(mo.notebook_location() / "public" / "penguins.csv")
#     df = pd.read_csv(fp)

#     # Drop rows with missing values for the relevant columns
#     plot_df = df.dropna(subset=["flipper_length_mm", "body_mass_g"])

#     def draw():
#         fig, ax = plt.subplots()
#         ax.scatter(plot_df["flipper_length_mm"], plot_df["body_mass_g"], alpha=0.7)
#         ax.set_xlabel("Flipper Length (mm)")
#         ax.set_ylabel("Body Mass (g)")
#         ax.set_title("Body Mass vs Flipper Length (mm)")
#         return fig

#     draw()


@app.cell
def _(mo):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the penguins dataset
    fp = str(mo.notebook_location() / "public" / "penguins.csv")
    df = pd.read_csv(fp)

    # Drop rows with missing values for the relevant columns
    plot_df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "species"])

    def draw():
        fig, ax = plt.subplots()
        species = plot_df["species"].unique()
        for sp in species:
            sp_df = plot_df[plot_df["species"] == sp]
            ax.scatter(
                sp_df["flipper_length_mm"],
                sp_df["body_mass_g"],
                alpha=0.7,
                label=sp
            )
        ax.set_xlabel("Flipper Length (mm)")
        ax.set_ylabel("Body Mass (g)")
        ax.set_title("Body Mass vs Flipper Length (mm) by Species")
        ax.legend(title="Species")
        return fig

    draw()