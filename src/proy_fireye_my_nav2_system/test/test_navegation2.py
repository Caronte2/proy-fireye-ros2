def test_check_sim_time():
    use_sim_time = True
    assert use_sim_time is True


def test_calculo_tiempo():
    t_ini = 10.0
    t_end = 15.0
    resultado = t_end - t_ini
    assert resultado == 5.0
