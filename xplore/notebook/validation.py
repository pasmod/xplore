def _check_if_target_is_set_when_mode_is_classification(mode=None, target=None):
    if mode == "classification":
        assert (
            target is not None
        ), "When mode=classification, a target variable should be defined."
