This document is a declaration of software quality for the `tracetools` package, based on the guidelines in [REP-2004](https://www.ros.org/reps/rep-2004.html).

# `tracetools` Quality Declaration

The package `tracetools` claims to be in the **Quality Level 1** category.

Below are the rationales, notes, and caveats for this claim, organized by each requirement listed in the [Package Requirements for Quality Level 1 in REP-2004](https://www.ros.org/reps/rep-2004.html).

## Version Policy [1]

### Version Scheme [1.i]

`tracetools` uses `semver` according to the recommendation for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#versioning).

### Version Stability [1.ii]

`tracetools` is at or above a stable version, i.e. `>= 1.0.0`.

**TODO** the current version is `0.3.0`.

### Public API Declaration [1.iii]

All symbols in the installed headers are considered part of the public API.

All installed headers are in the `include` directory of the package, headers in any other folders are not installed and considered private.

### API Stability Within a Released ROS Distribution [1.iv]/[1.vi]

`tracetools` will not break public API within a released ROS distribution, i.e. no major releases once the ROS distribution is released.

### ABI Stability Within a Released ROS Distribution [1.v]/[1.vi]

`tracetools` will maintain ABI stability within a ROS distribution.

## Change Control Process [2]

`tracetools` follows the recommended guidelines for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#change-control-process).

### Change Requests [2.i]

All changes occur through a merge request.

### Contributor Origin [2.ii]

All changes must have confirmation of contributor origin.

**TODO** set up DCO check

**TODO** what about past changes?

### Peer Review Policy [2.iii]

All merge requests must have at least one peer review.

### Continuous Integration [2.iv]

All merge requests must pass CI on all [tier 1 platforms](https://www.ros.org/reps/rep-2000.html#support-tiers).

**TODO** set up CI for arm64/macOS/Windows or find alternative

### Documentation Policy [2.v]

All merge requests must resolve related documentation changes before merging.

## Documentation [3]

`tracetools` follows the recommended guidelines for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#documentation).

### Feature Documentation [3.i]

`tracetools` has a [feature list](TODO) and each item in the list links to the corresponding feature documentation.
There is [documentation](../doc/design_ros_2.md) for all of the features, and new features require documentation before being added.

**TODO** add feature list and documentation

### Public API Documentation [3.ii]

`tracetools` has embedded API documentation for all of its public API, and new additions to the public API require documentation before being added.

**TODO** document API

### License [3.iii]

The license for `tracetools` is Apache 2.0, and a summary is in each source file, the type is declared in the `package.xml` manifest file, and a full copy of the license is in the [`LICENSE`](./LICENSE) file.

There is an automated test which runs a linter that ensures each file has a license statement.

### Copyright Statement [3.iv]

The copyright holders each provide a statement of copyright in each source code file in `tracetools`.

There is an automated test which runs a linter that ensures each file has at least one copyright statement.

## Testing [4]

### Feature Testing [4.i]

Each feature in `tracetools` has corresponding system tests which simulate typical usage, and they are located in the `tracetools_test` package.
New features are required to have tests before being added.

### Public API Testing [4.ii]

Each part of the public API has tests, and new additions or changes to the public API require tests before being added.
The tests aim to cover both typical usage and corner cases, but are quantified by contributing to code coverage.

### Coverage [4.iii]

`tracetools` follows the recommendations for ROS Core packages in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#code-coverage).

This includes:

- tracking and reporting line coverage statistics
- achieving and maintaining line coverage at or above 95%
- no lines are manually skipped in coverage calculations

Changes are required to make a best effort to keep or increase coverage before being accepted, but decreases are allowed if properly justified and accepted by reviewers.

Current coverage statistics can be viewed here:

**TODO** add code coverage visualization link

### Performance [4.iv]

**TODO**

### Linters and Static Analysis [4.v]

`tracetools` uses and passes all the standard linters and static analysis tools as described in the [ROS 2 Developer Guide](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#linters-and-static-analysis).

## Dependencies [5]

`tracetools` has a few "buildtool" dependencies, which do not affect the resulting quality of the package, because they do not contribute to the public library API.
It also has a few test dependencies, which do not affect the resulting quality of the package, because they are only used to build and run the test code.

### Direct Runtime ROS Dependencies [5.i]

### Optional Direct Runtime ROS Dependencies [5.ii]

### Direct Runtime non-ROS Dependency [5.iii]

`tracetools` has a run-time dependency on [LTTng](https://lttng.org/docs/v2.11/). It is stable, is tested extensively, has a strict version policy, and is designed for production systems. Therefore it is considered equivalent to **Quality Level 1**.

## Platform Support [6]

`tracetools` supports all of the tier 1 platforms as described in [REP-2000](https://www.ros.org/reps/rep-2000.html#support-tiers), and tests each change against all of them.
However, due to the nature of its features, they only work on Linux-based systems.

**TODO** same as [2.iv]
