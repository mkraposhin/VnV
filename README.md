# Verification and validation repository for QGD/Hybrid solvers

The primary objective of the repository to gather and keep updated verification and validation problems showing strengths and weakneses of the aforementioned computational complexes.

The structure of the repository is next.

1. On the first level go folders with titles of problems.
2. On the second level inside a problem folder we keep folders:
   - for reference data (reference/);
   - for literature (docs/);
   - for results of comparison (comparison/) with reference data and between different solvers;
   - for cases computed using different solvers (e.g., QGDFoam/, pimpleCentralFoam/, rhoCentralFoam/, etc);
   - for common data shared by different solvers (common/) cases.
3. On the third level, inside the solver folders we keep computational cases in folders with names specifying the mesh density (e.g., 10CPD, 20CPL, etc).

Together with this README.md on the first level we also keep the wish-list file containing the list of cases to run.
