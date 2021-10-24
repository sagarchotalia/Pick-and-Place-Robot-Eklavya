local simZMQ={}

function simZMQ.__init()
    -- wrap blocking functions with busy-wait loop:
    for func_name,flags_idx in pairs{msg_send=3,msg_recv=3,send=3,recv=2} do
        if not simZMQ['__'..func_name] then
            simZMQ['__'..func_name]=simZMQ[func_name]
            simZMQ[func_name]=function(...)
                local args={...}
                if sim.boolAnd32(args[flags_idx],simZMQ.DONTWAIT)>0 then
                    return simZMQ['__'..func_name](...)
                end
                args[flags_idx]=sim.boolOr32(args[flags_idx],simZMQ.DONTWAIT)
                while true do
                    local ret={simZMQ['__'..func_name](unpack(args))}
                    if ret[1]==-1 then
                        local err=simZMQ.errnum()
                        if err==simZMQ.EAGAIN then
                            sim.switchThread()
                        else
                            return -1,nil
                        end
                    else
                        return unpack(ret)
                    end
                end
            end
        end
    end
    -- initialize error-checking functions:
    simZMQ.__checkError={}
    simZMQ.__noError={}
    simZMQ.__raiseError={}
    for fn,f in pairs(simZMQ) do
        if type(f)=='function' then
            simZMQ.__checkError[fn]=function(...) end
            simZMQ.__noError[fn]=f
            simZMQ.__raiseError[fn]=function(...)
                local ret={simZMQ.__noError[fn](...)}
                simZMQ.__checkError[fn](unpack(ret))
                return unpack(ret)
            end
        end
    end
end

function simZMQ.__raiseErrors(enable)
    for fn,f in pairs(simZMQ) do
        if type(f)=='function' then
            if enable then
                simZMQ[fn]=simZMQ.__raiseError[fn]
            else
                simZMQ[fn]=simZMQ.__noError[fn]
            end
        end
    end
end

function simZMQ.__raise()
    error(simZMQ.strerror(simZMQ.errnum()))
end

simZMQ.__checkError={}

function simZMQ.__checkError.bind(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.close(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.connect(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.ctx_get(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.ctx_new(context)
    if context=='' then error() end
end

function simZMQ.__checkError.ctx_set(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.ctx_shutdown(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.ctx_term(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.disconnect(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.getsockopt(result,value)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_close(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_copy(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_gets(result,value)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_get(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_init_size(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_init(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_move(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_recv(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_send(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.msg_set(result)
    if result~=0 then simZMQ.__raise() end
end

function simZMQ.__checkError.poll(result,revents)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.proxy_steerable(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.proxy(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.recv(result,data)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.send(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.setsockopt(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.socket_monitor(result)
    if result<0 then simZMQ.__raise() end
end

function simZMQ.__checkError.unbind(result)
    if result~=0 then simZMQ.__raise() end
end

__initFunctions=__initFunctions or {}
table.insert(__initFunctions,simZMQ.__init)

return simZMQ
 