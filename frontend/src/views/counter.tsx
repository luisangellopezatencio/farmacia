import type { RootState } from "../app/store";
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement } from "../features/counter/counterSlice";


export default function CounterView() {
    const count = useSelector((state: RootState) => state.counter.value)
    const dispatch = useDispatch()

    return (
        <div>
            Count: {count}
            <button onClick={() => dispatch(increment())}>+</button>
            <button onClick={() => dispatch(decrement())}>-</button>
        </div>
    )
}